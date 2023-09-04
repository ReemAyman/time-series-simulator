import yaml
import re
from yaml.loader import SafeLoader
from pathlib import Path
import os

from time_series_configuration.configuration_reader.configuration_reader import ConfigurationReader


class YamlConfigurationReader(ConfigurationReader):
    """
    A class for reading configuration data with yaml file.
    """

    def __init__(self, file_name: str):
        if not re.findall(r"[.]yaml\b", file_name):
            raise ValueError("YamlConfigurationReader: File name should have the correct extension format '.yaml'")
        else:
            self.file_name = file_name

    def read_data(self) -> dict:
        """
        Read data from the yaml file.
        Returns:
            dict: A dictionary containing the data with (key, value) pair predefined in the yaml file read.
        """
        data = dict()
        parent_path = Path(__file__).parents[2]
        try:
            with open(os.path.join(parent_path, self.file_name), 'r') as f:
                data = yaml.load(f, Loader=SafeLoader)
        except FileNotFoundError:
            print("YamlConfigurationReader: File not found in the directory.")
        except Exception as e:
            print(e)
        return data
