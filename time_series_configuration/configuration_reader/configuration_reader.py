from abc import ABC, abstractmethod


class ConfigurationReader(ABC):
    """
    Abstract class for reading configurations.
    """
    @abstractmethod
    def read_data(self) -> dict:
        """
        Read the data from the defined source.
        Returns:
            dict: A dictionary containing the data with (key, value) pair.
        """
        pass
