import os

import pandas as pd

from confluent_kafka import Consumer

from time_series_data_consumer.consumer.time_series_data_consumer import TimeSeriesDataConsumer
from time_series_data_consumer.consumer_deserializer.consumer_deserializer_kafka import KafkaDeserializer


class TimeSeriesDataConsumerKafka(TimeSeriesDataConsumer):

    def __init__(self, topic, data_count):
        """
        Initializing time series data consumer in kafka.

        Args:
            topic: the kafka topic name data will be produced.
            data_count: the number of time series data simulated.

        """
        super().__init__(topic)
        self.data_count = data_count
        self.kafka_consumer = Consumer({
            'bootstrap.servers': 'host.docker.internal:9092',
            'group.id': 'G1',
            'auto.offset.reset': 'latest'
        })
        print(f'Consumer subscribed to: ${self.identifier}')
        self.kafka_consumer.subscribe([self.identifier])

    def consume_data(self):
        """
            Consumer time series data in a kafka topic.
        """
        # Poll for new messages from Kafka and print them.
        timeseries_dataframe = pd.DataFrame(columns=["attributeId", "value", "timestamp", "assetId"])
        received_data = 0
        try:
            while True:
                msg = self.kafka_consumer.poll(1.0)
                if received_data >= self.data_count:
                    break
                elif msg is None:

                    print("Waiting...")
                elif msg.error():
                    print("ERROR: %s".format(msg.error()))
                else:
                    timeseries_data = KafkaDeserializer(msg.value()).deserialize()
                    timeseries_dataframe.loc[len(timeseries_dataframe)] = timeseries_data
                    received_data += 1

                    print("Consumed event {received_data} out of {data_count} from topic {topic}: key = {key:12} value = {value:12}".format(
                        received_data=received_data, data_count=self.data_count, topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
        except Exception as e:
            print(e)

        print("Saving data in csv file ...")
        timeseries_file = 'consumer_data/'+self.identifier
        timeseries_dataframe.to_csv(timeseries_file + ".csv", mode='a',
                                    index=False, header=(not os.path.exists(timeseries_file+".csv")))

        print("Consumer close ...")
        self.kafka_consumer.close()
