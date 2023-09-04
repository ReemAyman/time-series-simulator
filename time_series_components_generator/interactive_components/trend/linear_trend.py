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
        if data_coefficients[0] != -1 and data_coefficients[0] != 1:
            raise ValueError("LinearTrend: Slope should be 1 or -1.")
        elif data_coefficients[1] < 0:
            raise ValueError("LinearTrend: Magnitude should be greater or equal to zero.")
        else:
            self.data_coefficients = data_coefficients

    def generate_data_component(self) -> Series:
        """
            Add polynomial trend component to the time series data.
        Returns:
            pandas.Series: The linear trend component of the time series.
        """

        trend_linear_component = np.zeros(len(self.time_interval_data))
        slope_value = -1 if self.data_coefficients[0] < 0 else 1
        if self.data_coefficients is not None:
            trend_linear_component = np.linspace(0, slope_value * self.data_coefficients[1],
                                                 len(self.time_interval_data))
        return Series(trend_linear_component)
