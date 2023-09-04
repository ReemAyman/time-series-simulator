import re

from time_series_data_store.time_series_data_store import TimeSeriesDataStore

import pandas as pd
from numpy import ndarray
from pathlib import Path
import os


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
        if re.findall(r"[.]", file_name):
            raise ValueError("TimeSeriesDataStoreCSV: File name should not contain '.'")
        else:
            self.file_name = file_name

    def store_data(self):
        """
            Store time series data in a .csv file format.
        """
        parent_path = Path(__file__).parents[1]
        df = pd.DataFrame({'value': self.generated_data, 'timestamp': self.time_interval})
        df.to_csv(os.path.join(parent_path, os.path.join('sample_datasets', self.file_name)) + '.csv', encoding='utf-8', index=False)
