from pandas import Series, DatetimeIndex
import numpy as np

from time_series_components_generator.interactive_components.trend.trend import Trend


class LinearTrend(Trend):

    def __init__(self, time_interval_data: DatetimeIndex, data_coefficients: np.ndarray):
        """
        Initialize the polynomial trend of time series data.

        Args:
            time_interval_data: the time intervals initialized by start time, end time, and frequency.
            data_coefficients: a numpy array of coefficients [slope(-1,1), magnitude] of the trend.
        """
        super().__init__(time_interval_data)
        self.data_coefficients = data_coefficients

    def generate_data_component(self) -> Series:
        """
            Add polynomial trend component to the time series data.
        Returns:
            pandas.Series: The linear trend component of the time series.
        """

        trend_linear_component = np.zeros(len(self.time_interval_data))
        for i, coefficient in enumerate(self.data_coefficients):
            time_intervals = np.arange(len(self.time_interval_data))
            trend_linear_component += coefficient * time_intervals ** i
        return Series(trend_linear_component)
