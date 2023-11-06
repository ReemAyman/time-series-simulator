from pandas import DataFrame

from time_series_data_producer.builder.producer_builder import ProducerBuilderInterface
from time_series_data_producer.producer.time_series_data_producer_kafka import TimeSeriesDataProducerKafka


class KafkaProducerBuilder(ProducerBuilderInterface):
    """
    A builder class to be used by a factory class for creating KafkaProducer instances to.

    """

    def __call__(self, generated_data: DataFrame, topic: str, generator_id, feature_id) -> TimeSeriesDataProducerKafka:
        """
        Create or retrieve a KafkaProducer instance.

        Parameters:
        - generated_data(pandas.DataFrame): the generated time series data.
        - topic (str): The topic where the KafkaProducer will produce to.
        - generator_id: the time series data generator id.
        - feature_id: the time series data feature id.

        Returns:
        - KafkaProducer: A KafkaProducer instance configured with the specified topic.

        """
        self._instance = TimeSeriesDataProducerKafka(generated_data, topic, generator_id, feature_id)
        return self._instance
