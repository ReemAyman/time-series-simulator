from abc import ABC, abstractmethod

from numpy import ndarray
from pandas import DatetimeIndex


class TimeSeriesDataStore(ABC):
    """
        Abstract class for storing time series data.
    """
    def __init__(self, generated_data: ndarray, time_interval: DatetimeIndex):
        """
        Initialize an instance for storing data.
        Args:
            generated_data: the time series generated data.
            time_interval: the time index of the data.
        """
        self.generated_data = generated_data
        self.time_interval = time_interval

    @abstractmethod
    def store_data(self) -> None:
        """
            Store the time series data generated.
        """
        pass
