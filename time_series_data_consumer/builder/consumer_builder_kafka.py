from time_series_data_consumer.builder.consumer_builder import ConsumerBuilderInterface
from time_series_data_consumer.consumer.time_series_data_consumer_kafka import TimeSeriesDataConsumerKafka


class KafkaConsumerBuilder(ConsumerBuilderInterface):
    """
    A builder class to be used by a factory class for creating KafkaConsumer instances to.

    """

    def __call__(self, topic: str, data_count) -> TimeSeriesDataConsumerKafka:
        """
        Create or retrieve a KafkaConsumer instance.

        Parameters:
        - topic (str): The topic where the KafkaConsumer will produce to.
        - data_count: the number of data instances generated.
        Returns:
        - KafkaConsumer: A KafkaConsumer instance configured with the specified topic.
        """
        self._instance = TimeSeriesDataConsumerKafka(topic, data_count)
        return self._instance
