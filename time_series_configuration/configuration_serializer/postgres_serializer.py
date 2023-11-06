
class PostgresSerializer:
    """
    A serializer for extracting specific fields from a database and returning them as a dictionary.

    """

    def __init__(self, config_data):
        """
        Initialize a PostgresSerializer instance.

        Parameters:
        - config_data: The database containing data to be serialized.

        """
        self.config_data = config_data

    def __dict__(self):
        """
        Serialize the database data into a dictionary.

        Returns:
        - dict: A dictionary containing selected fields from the database data.

        """
        return {
            "noise_level": self.config_data["noise_level"],
            "start_date": self.config_data["start_date"],
            "end_date": self.config_data["end_date"],
            "frequency": self.config_data["frequency"],
            "missings_percentage": self.config_data["missing_percentage"],
            "outliers_percentage": self.config_data["outlier_percentage"],
            "data_type": self.config_data["data_type"],
            "trend_coefficients": self.config_data["trend_coefficients"],
            "seasonality": self.config_data["seasonality_components"],
            "cyclic_period": self.config_data["cycle_frequency"],
            "cyclic_amplitude": self.config_data["cycle_amplitude"],
            "generator_id": self.config_data["generator_id"],
            "feature_id": self.config_data["feature_id"]
        }
