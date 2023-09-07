import unittest

import numpy as np
from pandas import DatetimeIndex, Series

from time_series_components_generator.interactive_components.seasonality.daily_seasonality import DailySeasonality
from time_series_components_generator.interactive_components.seasonality.seasonality import Seasonality


class TestDailySeasonality(unittest.TestCase):
    def test_daily_seasonality_creation_success(self):
        time_interval = DatetimeIndex(["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"])
        self.assertIsInstance(DailySeasonality(time_interval), Seasonality)

    def test_daily_seasonality_generate_data_component_success(self):
        time_interval = DatetimeIndex(["1/1/2020 10:00:00+00:00", "1/1/2020 11:00:00+00:00"])
        answer_generate_data = DailySeasonality(time_interval).generate_data_component()
        example_series = Series([0.49999999999999994, 0.258819045102521])
        self.assertTrue(np.array(example_series.values == answer_generate_data.values).all())


if __name__ == '__main__':
    unittest.main()
