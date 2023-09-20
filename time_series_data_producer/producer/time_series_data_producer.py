from abc import ABC, abstractmethod

from pandas import DataFrame


class TimeSeriesDataProducer(ABC):
    """
        Abstract class for storing time series data.
    """
    def __init__(self, generated_data: DataFrame, identifier: str):
        """
        Initialize an instance for storing data.
        Args:
            generated_data: the time series generated data.
            identifier: the placeholder where the data will be saved.
        """
        self.generated_data = generated_data
        self.identifier = identifier

    @abstractmethod
    def store_data(self) -> None:
        """
            Store the time series data generated.
        """
        pass
