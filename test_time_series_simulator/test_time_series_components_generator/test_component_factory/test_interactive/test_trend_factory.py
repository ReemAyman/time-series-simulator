import unittest

from pandas import DatetimeIndex

from time_series_components_generator.component_factory.interactive.interactive_component_factory import \
    InteractiveComponentFactory
from time_series_components_generator.component_factory.interactive.trend_factory import TrendFactory
from time_series_components_generator.interactive_components.trend.linear_trend import LinearTrend


class TestTrendFactory(unittest.TestCase):
    def setUp(self) -> None:
        time_interval = DatetimeIndex(["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"])
        trend_parameters = {"linear": [-1, 3]}
        self.trend_factory = TrendFactory(time_interval, trend_parameters)
        self.trend_dict = self.trend_factory.generate_components()

    def test_trend_factory_creation_success(self):
        self.assertIsInstance(self.trend_factory, InteractiveComponentFactory)

    def test_trend_generate_components_linear_exist(self):
        self.assertTrue(self.trend_dict.__contains__("linear"))

    def test_trend_generate_components_linear_created_success(self):
        self.assertIsInstance(self.trend_dict["linear"], LinearTrend)


if __name__ == '__main__':
    unittest.main()
