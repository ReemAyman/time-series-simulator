from pandas import Series
import numpy as np

from time_series_components_generator.interactive_components.seasonality.seasonality import Seasonality


class DailySeasonality(Seasonality):

    def generate_data_component(self) -> Series:
        """
            Add daily seasonality component to the time series data.

        Returns:
            pandas.Series: The daily seasonal component of the time series.
        """
        seasonal_daily_component = np.sin(2 * np.pi * self.time_interval_data.hour / 24)
        if self.data_type == "Additive":
            seasonal_daily_component += 1

        return Series(seasonal_daily_component)
