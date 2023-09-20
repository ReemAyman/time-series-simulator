from abc import ABC, abstractmethod

from pandas import DatetimeIndex

from time_series_components_generator.component_factory.time_series_component_factory import TimeSeriesComponentFactory
from time_series_components_generator.interactive_components.time_series_components import TimeSeriesComponent


class InteractiveComponentFactory(TimeSeriesComponentFactory, ABC):
    """
        An abstract class for generating interactive time series data (seasonality, trends)
    """

    def __init__(self, component_type: str, time_intervals: DatetimeIndex, **args):
        """
            Initializing time series component factory.
        Args:
            component_type: the type of the component to be extracted.
            time_intervals: the time intervals of the time series data.
        """
        self.time_intervals = time_intervals
        self.component_type = component_type

    @abstractmethod
    def generate_components(self) -> TimeSeriesComponent:
        pass
