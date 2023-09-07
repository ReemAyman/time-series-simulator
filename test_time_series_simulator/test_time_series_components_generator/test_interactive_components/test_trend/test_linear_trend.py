import unittest

import numpy as np
from pandas import DatetimeIndex, Series

from time_series_components_generator.interactive_components.trend.linear_trend import LinearTrend
from time_series_components_generator.interactive_components.trend.trend import Trend


class TestLinearTrend(unittest.TestCase):
    def test_quarterly_seasonality_creation_success(self):
        time_interval = DatetimeIndex(["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"])
        data_coefficients = [-1, 3]
        self.assertIsInstance(LinearTrend(time_interval, data_coefficients), Trend)

    def test_quarterly_seasonality_creation_slope_invalid_failure(self):
        time_interval = DatetimeIndex(["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"])
        data_coefficients = [-2, 3]
        self.assertRaises(ValueError, LinearTrend, time_interval, data_coefficients)

    def test_quarterly_seasonality_creation_magnitude_invalid_failure(self):
        time_interval = DatetimeIndex(["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"])
        data_coefficients = [-1, -1]
        self.assertRaises(ValueError, LinearTrend, time_interval, data_coefficients)

    def test_quarterly_seasonality_generate_data_component_success(self):
        time_interval = DatetimeIndex(["1/1/2020 10:00:00+00:00", "4/1/2020 11:00:00+00:00"])
        data_coefficients = [-1, 3]
        answer_generate_data = LinearTrend(time_interval, data_coefficients).generate_data_component()
        example_series = Series([0.0, -3.0])
        self.assertTrue(np.array(example_series.values == answer_generate_data.values).all())


if __name__ == '__main__':
    unittest.main()
