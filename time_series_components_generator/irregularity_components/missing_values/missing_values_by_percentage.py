import numpy as np

from time_series_components_generator.irregularity_components.missing_values.missing_values import MissingValues


class MissingValuesByPercentage(MissingValues):
    """Class for missing values in data by percentage."""

    def __init__(self, data_component_values: np.ndarray, percentage_missing: float = 0.05):
        super().__init__(data_component_values)
        self.percentage_missing = percentage_missing

    def generate_missing_values(self) -> np.ndarray:
        """
        Generate the missing values in data with the percentage of missing data randomly.

        Returns:
            numpy.ndarray: the data including the missing values.
        """
        num_missing = int(len(self.data_component_values) * self.percentage_missing)
        missing_indices = np.random.choice(len(self.data_component_values), size=num_missing, replace=False)

        data_with_missing_val = self.data_component_values.copy()
        data_with_missing_val[missing_indices] = np.nan

        return data_with_missing_val
