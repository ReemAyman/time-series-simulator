from time_series_configuration.configuration_reader.configuration_reader import ConfigurationReader
from time_series_configuration.configuration_serializer.postgres_serializer import PostgresSerializer


class PostgreReader(ConfigurationReader):

    def __init__(self, identifier):
        super().__init__(identifier)
        self.config_data = identifier
        self.serializer = PostgresSerializer(self.config_data)

    def read_data(self):
        return self.config_data

    def get_data(self, config_var_name: str):
        return self.serializer.__dict__()[config_var_name]
