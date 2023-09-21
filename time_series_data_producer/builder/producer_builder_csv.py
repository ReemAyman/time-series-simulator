from pandas import DataFrame

from time_series_data_producer.builder.producer_builder import ProducerBuilderInterface
from time_series_data_producer.producer.time_series_data_producer_csv import TimeSeriesDataProducerCSV


class CsvProducerBuilder(ProducerBuilderInterface):
    """
    A builder class to be used by a factory class for creating CsvProducer instances to.

    """

    def __call__(self, generated_data: DataFrame, location: str) -> TimeSeriesDataProducerCSV:
        """
        Create or retrieve a CsvProducer instance.

        Parameters:
        - generated_data(pandas.DataFrame): the generated time series data.
        - location (str): The location where the CsvProducer will generate CSV files.

        Returns:
        - CsvProducer: A CsvProducer instance configured with the specified location.

        """
        self._instance = TimeSeriesDataProducerCSV(generated_data, location)
        return self._instance
