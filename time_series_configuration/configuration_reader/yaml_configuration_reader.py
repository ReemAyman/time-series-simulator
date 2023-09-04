import yaml
from yaml.loader import SafeLoader

from time_series_configuration.configuration_reader.configuration_reader import ConfigurationReader


class YamlConfigurationReader(ConfigurationReader):
    """
    A class for reading configuration data with yaml file.
    """

    def __init__(self, file_name: str):
        self.file_name = file_name

    def read_data(self) -> dict:
        """
        Read data from the yaml file.
        Returns:
            dict: A dictionary containing the data with (key, value) pair predefined in the yaml file read.
        """
        with open(self.file_name, 'r') as f:
            data = yaml.load(f, Loader=SafeLoader)
        return data
