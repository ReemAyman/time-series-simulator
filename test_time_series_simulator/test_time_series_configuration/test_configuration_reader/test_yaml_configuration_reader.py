import unittest

from time_series_configuration.configuration_reader.configuration_reader import ConfigurationReader
from time_series_configuration.configuration_reader.yaml_configuration_reader import YamlReader


class TestYamlConfigurationReader(unittest.TestCase):
    def test_yaml_configuration_reader_creation_success(self):
        self.assertIsInstance(YamlReader("config.yaml"), ConfigurationReader)

    def test_yaml_configuration_reader_creation_invalid_filename_format(self):
        self.assertRaises(ValueError, YamlReader, "con.y")

    def test_yaml_configuration_reader_read_data_success(self):
        self.assertNotEqual(YamlReader("data_config.yaml").read_data(), dict())

    def test_yaml_configuration_reader_read_data_failure(self):
        self.assertEqual(YamlReader("config.yaml").read_data(), dict())


if __name__ == '__main__':
    unittest.main()
