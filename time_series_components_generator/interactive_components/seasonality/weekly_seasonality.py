from pandas import Series
import numpy as np

from time_series_components_generator.interactive_components.seasonality.seasonality import Seasonality


class WeeklySeasonality(Seasonality):

    def generate_data_component(self) -> Series:
        """
            Add weekly seasonality component to the time series data.

        Returns:
            pandas.Series: The weekly seasonal component of the time series.
        """
        seasonal_weekly_component = self.amplitude * np.sin(
                2 * np.pi * (self.time_interval_data.day / (7 * self.seasonality_multiplier)) + self.phase_shift)

        return Series(seasonal_weekly_component)
