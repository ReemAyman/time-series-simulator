from pandas import Series
import numpy as np

from time_series_components_generator.interactive_components.trend.trend import Trend


class PolynomialTrend(Trend):

    def __init__(self, data_coefficients: np.ndarray):
        """
        Initialize the polynomial trend of time series data.

        Args:
            data_coefficients: a numpy array of coefficients [a0, a1, a2, ...] of the polynomial equation (a0 + a1*t + a2*t^2 + ....)
        """
        super().__init__(self.time_interval_data)
        self.data_coefficients = data_coefficients

    def generate_data_component(self) -> Series:
        """
            Add polynomial trend component to the time series data.
        Returns:
            pandas.Series: The polynomial trend component of the time series.
        """
        if self.data_coefficients is not None:
            trend_polynomial_component = 0
            current_data_interval = np.ones(self.time_interval_data)

            # Calculate the trend polynomial component by multiplying the coefficient by the corresponding polynomial power
            for coefficient in self.data_coefficients:
                trend_polynomial_component += coefficient * current_data_interval
                current_data_interval *= self.time_interval_data

        return Series(trend_polynomial_component)
