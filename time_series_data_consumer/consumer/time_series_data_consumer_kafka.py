import json

import pandas as pd
# from pandas import DataFrame
from confluent_kafka import Consumer
# from confluent_kafka.schema_registry.json_schema import JSONDeserializer


class TimeSeriesDataConsumerKafka:

    def __init__(self, topic, data_count):
        """
        Initializing time series data consumer in kafka.

        Args:
            topic: the kafka topic name data will be produced.
            data_count: the number of time series data simulated.

        """
        self.topic = topic
        self.data_count = data_count
        self.kafka_consumer = Consumer({
            'bootstrap.servers': 'host.docker.internal:9092',
            'group.id': 'G1',
            'auto.offset.reset': 'latest'
        })
        print(f'Consumer subscribed to: ${self.topic}')
        self.kafka_consumer.subscribe([self.topic])

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
                    # Initial message consumption may take up to
                    # `session.timeout.ms` for the consumer group to
                    # Re-balance and start consuming
                    print("Waiting...")
                elif msg.error():
                    print("ERROR: %s".format(msg.error()))

                else:
                    timeseries_data = json.loads(msg.value())
                    timeseries_dataframe.loc[len(timeseries_dataframe)] = timeseries_data
                    received_data += 1
                    # Extract the (optional) key and value, and print.
                    print("Consumed event {received_data} out of {data_count} from topic {topic}: key = {key:12} value = {value:12}".format(
                        received_data=received_data, data_count=self.data_count, topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
        except Exception as e:
            print(e)

        print("Saving data in csv file ...")
        timeseries_file = 'consumer_data/'+self.topic
        timeseries_dataframe.to_csv(timeseries_file + ".csv", mode='a', index=False)
        print("Consumer close ...")
        self.kafka_consumer.close()
