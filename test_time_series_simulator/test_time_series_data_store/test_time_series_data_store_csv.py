import unittest

import numpy as np
from pandas import DatetimeIndex

from time_series_data_store.time_series_data_store import TimeSeriesDataStore
from time_series_data_store.time_series_data_store_csv import TimeSeriesDataStoreCSV


class TestTimeSeriesDataStoreCSV(unittest.TestCase):
    def test_time_series_data_store_csv_creation_success(self):
        time_interval = DatetimeIndex(["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"])
        time_series_data = np.array([-0.7188723889039199, -1.1109419085035253])
        self.assertIsInstance(TimeSeriesDataStoreCSV(time_series_data, time_interval, "12"),
                              TimeSeriesDataStore)

    def test_time_series_data_store_csv_creation_invalid_filename_format(self):
        time_interval = DatetimeIndex(["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"])
        time_series_data = np.array([-0.7188723889039199, -1.1109419085035253])
        self.assertRaises(ValueError, TimeSeriesDataStoreCSV, time_series_data, time_interval, "12.csv")

    def test_time_series_data_store_csv_store_data_success(self):
        time_interval = DatetimeIndex(["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"])
        time_series_data = np.array([-0.7188723889039199, -1.1109419085035253])
        self.assertIsNone(TimeSeriesDataStoreCSV(time_series_data, time_interval, "12").store_data())


if __name__ == '__main__':
    unittest.main()
