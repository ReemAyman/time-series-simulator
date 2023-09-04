from time_series_components_generator.component_factory.interactive.interactive_component_factory import \
    InteractiveComponentFactory
from time_series_components_generator.interactive_components.seasonality.daily_seasonality import DailySeasonality
from time_series_components_generator.interactive_components.seasonality.quarterly_seasonality import \
    QuarterlySeasonality
from time_series_components_generator.interactive_components.seasonality.weekly_seasonality import WeeklySeasonality


class SeasonalityFactory(InteractiveComponentFactory):
    """
        A class for generating seasonality different types.
    """

    def generate_components(self) -> dict:
        """
            Generate seasonality instances for different types from the time index.

        Returns:
             dict: A dictionary contains different types of seasonalities.
        """
        seasonality_dict = {"daily": DailySeasonality(self.time_intervals),
                            "weekly": WeeklySeasonality(self.time_intervals), "quarterly": QuarterlySeasonality(self.time_intervals)}
        return seasonality_dict
