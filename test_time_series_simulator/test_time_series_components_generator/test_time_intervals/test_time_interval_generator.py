import unittest
from datetime import datetime

from pandas import DatetimeIndex

from time_series_components_generator.time_intervals.time_series_generator import TimeSeriesGenerator


class TestTimeIntervalGenerator(unittest.TestCase):

    def test_generate_time_interval_success(self):
        start_date = datetime(2021, 1, 1)
        end_date = datetime(2021, 2, 1)
        frequency = "12H"
        time_interval_generator = TimeSeriesGenerator(start_date, end_date, frequency)
        self.assertIsInstance(time_interval_generator.generate_time_interval(), DatetimeIndex)

    def test_generate_time_interval_start_after_end_date_empty_success(self):
        start_date = datetime(2021, 2, 1)
        end_date = datetime(2021, 1, 1)
        frequency = "12H"
        time_interval_generator = TimeSeriesGenerator(start_date, end_date, frequency)
        self.assertTrue(time_interval_generator.generate_time_interval().empty)

    def test_generate_time_interval_start_frequency_format_failure(self):
        start_date = datetime(2021, 1, 1)
        end_date = datetime(2021, 2, 1)
        frequency = "12"
        time_interval_generator = TimeSeriesGenerator(start_date, end_date, frequency)
        self.assertRaises(ValueError, time_interval_generator.generate_time_interval)


if __name__ == '__main__':
    unittest.main()
