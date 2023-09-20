import yaml
import re
from yaml.loader import SafeLoader

from time_series_configuration.configuration_reader.configuration_reader import ConfigurationReader
from time_series_configuration.configuration_serializer.yaml_serializer import YamlSerializer


class YamlReader(ConfigurationReader):
    """
    A class for reading configuration data with yaml file.
    """
    def __init__(self, identifier):
        if not (re.findall(r"[.]yaml\b", identifier) or re.findall(r"[.]yml\b", identifier)):
            raise ValueError("YamlConfigurationReader: File name should have the correct extension format '.yaml'")
        else:
            super().__init__(identifier)
            self.file = self.read_data()
            self.serializer = YamlSerializer(self.file)

    def read_data(self) -> dict:
        """
            Read data from the yaml file.
        Returns:
            dict: A dictionary containing the data with (key, value) pair predefined in the yaml file read.
        """
        data = dict()
        try:
            with open(self.identifier, 'r') as f:
                data = yaml.load(f, Loader=SafeLoader)
        except FileNotFoundError:
            print("YamlConfigurationReader: File not found in the directory.")
        except Exception as e:
            print(e)
        return data

    def get_data(self, config_var_name: str):
        """
            Get a specific configuration variable from the YAML data.
        Parameters:
        - config_var_name: The name of the configuration variable.

        Returns:
        - Any: The value of the specified configuration variable from the YAML data.

        """
        return self.serializer.__dict__()[config_var_name]
