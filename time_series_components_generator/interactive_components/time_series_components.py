from abc import ABC, abstractmethod
from pandas import DatetimeIndex, Series


class TimeSeriesComponent(ABC):
    """
    An abstract class for time series component (Seasonality, Trend, and Cyclicity).
    """
    def __init__(self, time_interval_data: DatetimeIndex):
        """
        Initializing time series component.

        Args:
            time_interval_data: the time intervals initialized by start time, end time, and frequency.
        """
        self.time_interval_data = time_interval_data

    @abstractmethod
    def generate_data_component(self) -> Series:
        """
        Generates time series data according to its type.
        """
        pass
