
class YamlSerializer:
    """
    A serializer for extracting specific fields from a YAML file and returning them as a dictionary.

    """

    def __init__(self, yaml_file):
        """
        Initialize a YamlSerializer instance.

        Parameters:
        - yaml_file: The YAML file containing data to be serialized.

        """
        self.file = yaml_file

    def __dict__(self):
        """
        Serialize the YAML data into a dictionary.

        Returns:
        - dict: A dictionary containing selected fields from the YAML data.

        """
        return {
            "noise_level": self.file["noise_level"],
            "start_date": self.file["start_date"],
            "end_date": self.file["end_date"],
            "frequency": self.file["frequency"],
            "missings_percentage": self.file["missings_percentage"],
            "outliers_percentage": self.file["outliers_percentage"],
            "data_type": self.file["data_type"],
            "trend_coefficients": self.file["trend_coefficients"],
            "seasonality": self.file["seasonality"],
            "cyclic_period": self.file["cyclic_period"],
            "cyclic_amplitude": self.file["cyclic_amplitude"],
        }
