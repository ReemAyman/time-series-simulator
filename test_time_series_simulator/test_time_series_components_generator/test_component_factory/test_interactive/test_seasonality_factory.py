import unittest

from pandas import DatetimeIndex

from time_series_components_generator.component_factory.interactive.interactive_component_factory import \
    InteractiveComponentFactory
from time_series_components_generator.component_factory.interactive.seasonality_factory import SeasonalityFactory
from time_series_components_generator.interactive_components.seasonality.daily_seasonality import DailySeasonality
from time_series_components_generator.interactive_components.seasonality.quarterly_seasonality import \
    QuarterlySeasonality
from time_series_components_generator.interactive_components.seasonality.weekly_seasonality import WeeklySeasonality


class TestSeasonalityFactory(unittest.TestCase):
    def setUp(self) -> None:
        time_interval = DatetimeIndex(["1/1/2020 10:00:00+00:00", "2/1/2020 11:00:00+00:00"])
        self.seasonality_factory = SeasonalityFactory(time_interval)
        self.seasonality_dict = self.seasonality_factory.generate_components()

    def test_seasonality_factory_creation_success(self):
        self.assertIsInstance(self.seasonality_factory, InteractiveComponentFactory)

    def test_seasonality_generate_components_daily_exist(self):
        self.assertTrue(self.seasonality_dict.__contains__("daily"))

    def test_seasonality_generate_components_weekly_exist(self):
        self.assertTrue(self.seasonality_dict.__contains__("weekly"))

    def test_seasonality_generate_components_quarterly_exist(self):
        self.assertTrue(self.seasonality_dict.__contains__("quarterly"))

    def test_seasonality_generate_components_daily_created_success(self):
        self.assertIsInstance(self.seasonality_dict["daily"], DailySeasonality)

    def test_seasonality_generate_components_weekly_created_success(self):
        self.assertIsInstance(self.seasonality_dict["weekly"], WeeklySeasonality)

    def test_seasonality_generate_components_quarterly_created_success(self):
        self.assertIsInstance(self.seasonality_dict["quarterly"], QuarterlySeasonality)


if __name__ == '__main__':
    unittest.main()
