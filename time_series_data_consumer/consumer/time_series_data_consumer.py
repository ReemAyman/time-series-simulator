from abc import ABC, abstractmethod


class TimeSeriesDataConsumer(ABC):
    """
        Abstract class for consuming time series data.
    """
    def __init__(self, identifier: str):
        """
        Initialize an instance for storing data.
        Args:
            identifier: the placeholder where the data will be consumed.
        """
        self.identifier = identifier

    @abstractmethod
    def consume_data(self) -> None:
        """
            Consume the time series data generated.
        """
        pass
