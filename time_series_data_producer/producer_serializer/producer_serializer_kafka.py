import json

from kafka_message.kafka_message import TimeSeriesKafkaMessage
from time_series_data_producer.producer_serializer.producer_serializer import ProducerSerializer


class KafkaSerializer(ProducerSerializer):
    """
    A class for serializing kafka messages.
    """
    def __init__(self, kafka_message: TimeSeriesKafkaMessage):
        super().__init__(kafka_message)

    def serialize(self):
        """
        Serializing data as json for kafka producer.
        Returns:
            Json data as string representing kafka message.
        """
        return json.dumps(self.serializable.__dict__())
