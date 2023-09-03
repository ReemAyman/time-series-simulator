from pandas import Series
import numpy as np

from time_series_components_generator.interactive_components.seasonality.seasonality import Seasonality


class QuarterlySeasonality(Seasonality):

    def generate_data_component(self) -> Series:
        """
            Add weekly seasonality component to the time series data.

        Returns:
            pandas.Series: The weekly seasonal component of the time series.
        """
        seasonal_quarterly_component = np.sin(2 * np.pi * (self.time_interval_data.quarter - 1) / 4)
        if self.data_type == "Additive":
            seasonal_quarterly_component += 1

        return Series(seasonal_quarterly_component)
