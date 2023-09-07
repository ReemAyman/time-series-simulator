import unittest

import numpy as np
from pandas import DatetimeIndex, Series

from time_series_components_generator.interactive_components.seasonality.weekly_seasonality import WeeklySeasonality
from time_series_components_generator.interactive_components.seasonality.seasonality import Seasonality


class TestWeeklySeasonality(unittest.TestCase):
    def test_weekly_seasonality_creation_success(self):
        time_interval = DatetimeIndex(["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"])
        self.assertIsInstance(WeeklySeasonality(time_interval), Seasonality)

    def test_weekly_seasonality_generate_data_component_success(self):
        time_interval = DatetimeIndex(["1/1/2020 10:00:00+00:00", "10/1/2020 11:00:00+00:00"])
        answer_generate_data = WeeklySeasonality(time_interval).generate_data_component()
        example_series = Series([0.9749279121818236, 0.43388373911755823])
        self.assertTrue(np.array(example_series.values == answer_generate_data.values).all())


if __name__ == '__main__':
    unittest.main()
