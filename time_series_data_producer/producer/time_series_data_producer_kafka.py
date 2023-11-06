import json

from pandas import DataFrame
from confluent_kafka import Producer
# from confluent_kafka.schema_registry.json_schema import JSONSerializer
# from confluent_kafka.serialization import StringSerializer

from kafka_message.kafka_message import TimeSeriesKafkaMessage
from time_series_data_producer.producer.time_series_data_producer import TimeSeriesDataProducer


class TimeSeriesDataProducerKafka(TimeSeriesDataProducer):

    def __init__(self, generated_data: DataFrame, identifier, generator_id, feature_id):
        """
        Initializing time series data store in kafka.

        Args:
            generated_data: the time series generated data.
            identifier: the kafka topic name data will be produced.
            generator_id: the time series data generator id.
            feature_id: the time series data feature id.
        """
        super().__init__(generated_data, identifier)
        self.generator_id = generator_id
        self.feature_id = feature_id

        self.kafka_producer = Producer({
            'bootstrap.servers': 'host.docker.internal:9092',
        })

    def store_data(self):
        """
            Produce time series data in a kafka topic.
        """
        print("Kafka produce data ...")
        for i, data_instance in self.generated_data.iterrows():

            time_series_kafka = TimeSeriesKafkaMessage(
                self.feature_id, data_instance["value"], data_instance["timestamp"], self.generator_id)
            value = json.dumps(time_series_kafka.__dict__())
            key = str(self.generator_id + self.feature_id + str(i))

            # Produce asynchronously with delivery callback
            self.kafka_producer.produce(self.identifier, key=key, value=value, callback=self.delivery_callback)

        # Wait for any outstanding messages to be delivered and delivery report callbacks to be triggered
        self.kafka_producer.flush(10.0)

    @staticmethod
    def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
