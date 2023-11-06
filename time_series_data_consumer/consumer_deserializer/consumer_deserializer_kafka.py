import json

from time_series_data_consumer.consumer_deserializer.consumer_deserializer import ConsumerDeserializer


class KafkaDeserializer(ConsumerDeserializer):
    """
    A class for deserializing kafka messages.
    """
    def __init__(self, kafka_message):
        super().__init__(kafka_message)

    def deserialize(self):
        """
        Deserializing data as json from kafka consumer.
        Returns:
            Json data as dictionary representing kafka message.
        """
        return json.loads(self.deserializable)
