import unittest

import numpy as np
from pandas import DatetimeIndex, Series

from time_series_components_generator.interactive_components.seasonality.quarterly_seasonality import QuarterlySeasonality
from time_series_components_generator.interactive_components.seasonality.seasonality import Seasonality


class TestQuarterlySeasonality(unittest.TestCase):
    def test_quarterly_seasonality_creation_success(self):
        time_interval = DatetimeIndex(["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"])
        self.assertIsInstance(QuarterlySeasonality(time_interval), Seasonality)

    def test_quarterly_seasonality_generate_data_component_success(self):
        time_interval = DatetimeIndex(["1/1/2020 10:00:00+00:00", "4/1/2020 11:00:00+00:00"])
        answer_generate_data = QuarterlySeasonality(time_interval).generate_data_component()
        example_series = Series([0.0, 1.0])
        self.assertTrue(np.array(example_series.values == answer_generate_data.values).all())


if __name__ == '__main__':
    unittest.main()
