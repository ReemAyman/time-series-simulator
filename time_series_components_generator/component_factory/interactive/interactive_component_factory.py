from abc import ABC

from pandas import DatetimeIndex

from time_series_components_generator.component_factory.time_series_component_factory import TimeSeriesComponentFactory


class InteractiveComponentFactory(TimeSeriesComponentFactory, ABC):
    """
        An abstract class for generating interactive time series data (seasonality, trends)
    """

    def __init__(self, time_intervals: DatetimeIndex):
        """
            Initializing time series component factory.
        Args:
            time_intervals: the time intervals of the time series data.
        """
        self.time_intervals = time_intervals
