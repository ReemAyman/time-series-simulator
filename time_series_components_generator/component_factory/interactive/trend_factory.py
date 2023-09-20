import numpy as np
from pandas import DatetimeIndex

from time_series_components_generator.component_factory.interactive.interactive_component_factory import \
    InteractiveComponentFactory
from time_series_components_generator.interactive_components.trend.linear_trend import LinearTrend
from time_series_components_generator.interactive_components.trend.trend import Trend


class TrendFactory(InteractiveComponentFactory):
    """
        A class for generating trend different types.
    """

    def __init__(self, component_type: str, time_intervals: DatetimeIndex,  trend_parameters: dict):
        """
            Initializing trend factory.
        Args:
            time_intervals: the time intervals of the time series data.
            trend_parameters: the parameters of the trend of different types.
        """
        super().__init__(component_type, time_intervals)
        self.trend_parameters = trend_parameters

    def generate_components(self) -> Trend:
        """
            Generate trend instances for different types from the time index.

        Returns:
             dict: A dictionary contains different types of trends.
        """
        trend_dict = {"Linear": LinearTrend(self.time_intervals, np.array(self.trend_parameters["linear"]))}
        return trend_dict[self.component_type]
