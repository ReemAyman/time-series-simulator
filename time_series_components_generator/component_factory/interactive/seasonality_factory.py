from pandas import DatetimeIndex

from time_series_components_generator.component_factory.interactive.interactive_component_factory import \
    InteractiveComponentFactory
from time_series_components_generator.interactive_components.seasonality.daily_seasonality import DailySeasonality
from time_series_components_generator.interactive_components.seasonality.monthly_seasonality import \
    MonthlySeasonality
from time_series_components_generator.interactive_components.seasonality.seasonality import Seasonality
from time_series_components_generator.interactive_components.seasonality.weekly_seasonality import WeeklySeasonality


class SeasonalityFactory(InteractiveComponentFactory):
    """
        A class for generating seasonality different types.
    """

    def __init__(self, component_type: str, time_intervals: DatetimeIndex, amplitude, seasonality_multiplier, phase_shift):
        super().__init__(component_type, time_intervals)
        self.amplitude = amplitude
        self.seasonality_multiplier = seasonality_multiplier
        self.phase_shift = phase_shift

    def generate_components(self) -> Seasonality:
        """
            Generate seasonality instances for different types from the time index.

        Returns:
             dict: A dictionary contains different types of seasonalities.
        """
        seasonality_dict = {"Daily": DailySeasonality(self.time_intervals, self.amplitude, self.seasonality_multiplier, self.phase_shift),
                            "Weekly": WeeklySeasonality(self.time_intervals, self.amplitude, self.seasonality_multiplier, self.phase_shift),
                            "Monthly": MonthlySeasonality(self.time_intervals, self.amplitude, self.seasonality_multiplier, self.phase_shift)}
        return seasonality_dict[self.component_type]
