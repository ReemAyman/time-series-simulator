from abc import ABC, abstractmethod


class TimeSeriesComponentFactory(ABC):
    """
    An abstract class for generating time series components for different types.
    """

    @abstractmethod
    def generate_components(self) -> dict:
        """
            Generate component different types.
        Returns:
            dict: A dictionary containing the different component types with its corresponding keys.
        """
        pass
