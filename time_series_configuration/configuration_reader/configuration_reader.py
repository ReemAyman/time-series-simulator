from abc import ABC, abstractmethod


class ConfigurationReader(ABC):
    """
    Abstract class for reading configurations.
    """
    def __init__(self, identifier):
        self.identifier = identifier

    @abstractmethod
    def read_data(self):
        """
            Read the data from the defined source.
        """
        pass

    @abstractmethod
    def get_data(self, config_var_name: str):
        """

        Args:
            config_var_name:

        Returns:

        """
        pass
