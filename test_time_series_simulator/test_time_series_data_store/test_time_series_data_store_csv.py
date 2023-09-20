import unittest

import numpy as np
from pandas import DatetimeIndex

from time_series_data_producer.producer.time_series_data_producer import TimeSeriesDataProducer
from time_series_data_producer.producer.time_series_data_producer_csv import TimeSeriesDataProducerCSV


class TestTimeSeriesDataStoreCSV(unittest.TestCase):
    def test_time_series_data_store_csv_creation_success(self):
        time_interval = DatetimeIndex(["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"])
        time_series_data = np.array([-0.7188723889039199, -1.1109419085035253])
        self.assertIsInstance(TimeSeriesDataProducerCSV(time_series_data, "12"),
                              TimeSeriesDataProducer)

    def test_time_series_data_store_csv_creation_invalid_filename_format(self):
        time_interval = DatetimeIndex(["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"])
        time_series_data = np.array([-0.7188723889039199, -1.1109419085035253])
        self.assertRaises(ValueError, TimeSeriesDataProducerCSV, time_series_data, time_interval, "12.csv")

    def test_time_series_data_store_csv_store_data_success(self):
        time_interval = DatetimeIndex(["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"])
        time_series_data = np.array([-0.7188723889039199, -1.1109419085035253])
        self.assertIsNone(TimeSeriesDataProducerCSV(time_series_data, "12").store_data())


if __name__ == '__main__':
    unittest.main()
