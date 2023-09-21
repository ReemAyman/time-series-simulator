from time_series_components_generator.data_type_enum import DataTypeEnum


class ConfigurationFacade:
    """
    A facade class for accessing configuration data through a reader.
    """

    def __init__(self, reader):
        """
        Initialize a ConfigurationFacade instance.

        Parameters:
        - reader: An instance of a configuration reader.

        """
        self.reader = reader

    @property
    def cyclic_period(self):
        """
        Get the cyclic period ( in years)  from the configuration ,

        Returns:
        - float : The cyclic period specified in the configuration.
        """
        return float(self.reader.get_data("cyclic_period"))

    @property
    def cyclic_amplitude(self):
        """
        Get the cyclic amplitude from the configuration.

        Returns:
        - float : The cyclic amplitude specified in the configuration.
        """
        return float(self.reader.get_data("cyclic_amplitude"))

    @property
    def noise_level(self):
        """
        Get the noise level from the configuration.

        Returns:
        - float: The noise level specified in the configuration.
        """
        return self.reader.get_data("noise_level")

    @property
    def start_date(self):
        """
        Get the start date from the configuration.

        Returns:
        - string: The start date specified in the configuration.
        """
        return self.reader.get_data("start_date")

    @property
    def end_date(self):
        """
        Get the end date from the configuration.

        Returns:
        - string: The end date specified in the configuration.
        """
        return self.reader.get_data("end_date")

    @property
    def seasonality(self):
        """
        Get the seasonality from the configuration.

        Returns:
        - list[dict]: The seasonality componenets specified in the configuration.
        """
        return self.reader.get_data("seasonality")

    @property
    def frequency(self):
        """
        Get the frequency from the configuration.

        Returns:
        - string: The frequency specified in the configuration.
        """
        return self.reader.get_data("frequency")

    @property
    def trend_coefficients(self):
        """
        Get the trend coefficients from the configuration.

        Returns:
        - List[float]: A list of trend coefficients specified in the configuration.
        """
        return self.reader.get_data("trend_coefficients")

    @property
    def percentage_outliers(self):
        """
        Get the percentage of outliers from the configuration.

        Returns:
        - float: The percentage of outliers specified in the configuration.
        """
        return float(self.reader.get_data("outliers_percentage"))

    @property
    def missings_percentage(self):
        """
        Get the missing data percentage from the configuration.

        Returns:
        - float: The missing data percentage specified in the configuration.
        """
        return float(self.reader.get_data("missings_percentage"))

    @property
    def data_type(self):
        """
        Get the data type from the configuration.

        Returns:
        - str: The data type specified in the configuration, as a string.
        """
        return DataTypeEnum[self.reader.get_data("data_type")].value
