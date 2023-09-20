import re

from time_series_data_producer.producer.time_series_data_producer import TimeSeriesDataProducer

from pandas import DataFrame
import os


class TimeSeriesDataProducerCSV(TimeSeriesDataProducer):

    def __init__(self, generated_data: DataFrame, identifier):
        """
        Initializing time series data store in csv.

        Args:
            generated_data: the time series generated data.
            identifier: the file name data will be saved.
        """
        super().__init__(generated_data, identifier)
        if not re.findall(r"[.]", identifier):
            raise ValueError("TimeSeriesDataStoreCSV: File name should contain '.'")
        else:
            self._check_identifier_exits_or_create()

    def _check_identifier_exits_or_create(self):
        directory_path = os.path.dirname(self.identifier)
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)

    def store_data(self):
        """
            Store time series data in a .csv file format.
        """
        self.generated_data.to_csv(self.identifier, encoding='utf-8', index=False)
