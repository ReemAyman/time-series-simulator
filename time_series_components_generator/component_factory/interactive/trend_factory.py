import numpy as np
from pandas import DatetimeIndex

from time_series_components_generator.component_factory.interactive.interactive_component_factory import \
    InteractiveComponentFactory
from time_series_components_generator.interactive_components.trend.polynomial_trend import PolynomialTrend


class TrendFactory(InteractiveComponentFactory):
    """
        A class for generating trend different types.
    """

    def __init__(self, time_intervals: DatetimeIndex, trend_parameters: dict):
        """
            Initializing trend factory.
        Args:
            time_intervals: the time intervals of the time series data.
            trend_parameters: the parameters of the trend of different types.
        """
        super().__init__(time_intervals)
        self.trend_parameters = trend_parameters

    def generate_components(self) -> dict:
        """
            Generate trend instances for different types from the time index.

        Returns:
             dict: A dictionary contains different types of trends.
        """
        trend_dict = {"polynomial": PolynomialTrend(self.time_intervals, np.array(self.trend_parameters["polynomial"]))}
        return trend_dict
