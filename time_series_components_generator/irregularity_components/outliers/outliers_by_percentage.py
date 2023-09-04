import numpy as np

from time_series_components_generator.irregularity_components.outliers.outliers import Outliers


class OutliersByPercentage(Outliers):
    """Class for outliers in data by percentage."""

    def __init__(self, data_component_values: np.ndarray, percentage_outliers: float = 0.05):
        """
            Initializing percentage outliers by parameters needed.
        Args:
            data_component_values: the data component after constructing seasonality, cyclicity, and trend across time intervals.
            percentage_outliers: the percentage of the outliers across the generated data.
        """
        super().__init__(data_component_values)
        if 0 <= percentage_outliers <= 1:
            self.percentage_outliers = percentage_outliers
        else:
            raise ValueError("OutliersByPercentage: Percentage value should be of range [0, 1]")

    def generate_outliers(self) -> np.ndarray:
        """
        Generate the data including outliers with percentage.

        Returns:
            numpy.ndarray: A numpy array including the data after adding the outliers.
        """
        num_outliers = int(len(self.data_component_values) * self.percentage_outliers)
        outlier_indices = np.random.choice(len(self.data_component_values), num_outliers, replace=False)

        data_with_outliers = self.data_component_values.copy()
        outliers = np.random.uniform(-1, 1, num_outliers)
        anomaly_mask = np.zeros(len(data_with_outliers), dtype=bool)

        if len(outliers) > 0:
            data_with_outliers[outlier_indices] = outliers
            anomaly_mask[outlier_indices] = True

        return data_with_outliers
