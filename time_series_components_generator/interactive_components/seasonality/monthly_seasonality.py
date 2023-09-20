from pandas import Series
import numpy as np

from time_series_components_generator.interactive_components.seasonality.seasonality import Seasonality


class MonthlySeasonality(Seasonality):

    def generate_data_component(self) -> Series:
        """
            Add monthly seasonality component to the time series data.

        Returns:
            pandas.Series: The monthly seasonal component of the time series.
        """
        seasonal_monthly_component = self.amplitude * np.sin(
                2 * np.pi * (self.time_interval_data.dayofyear / (30 * self.seasonality_multiplier)) + self.phase_shift)

        return Series(seasonal_monthly_component)
