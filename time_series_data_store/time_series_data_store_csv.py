from time_series_data_store.time_series_data_store import TimeSeriesDataStore

import pandas as pd
from numpy import ndarray


class TimeSeriesDataStoreCSV(TimeSeriesDataStore):

    def __init__(self, generated_data: ndarray, time_interval: pd.DatetimeIndex, file_name: str):
        """
        Initializing time series data store in csv.

        Args:
            generated_data: the time series generated data.
            time_interval: the time index of the data.
            file_name: the file name data will be saved.
        """
        super().__init__(generated_data, time_interval)
        self.file_name = file_name

    def store_data(self):
        """
            Store time series data in a .csv file format.
        """
        df = pd.DataFrame({'value': self.generated_data, 'timestamp': self.time_interval})
        df.to_csv('sample_datasets/' + str(self.file_name) + '.csv', encoding='utf-8', index=False)
