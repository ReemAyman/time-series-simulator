import numpy as np

from time_series_components_generator.trasformers.transformer import Transformer


class OutlierTransformer(Transformer):
    """Class for outliers in data by percentage."""

    def __init__(self, percentage_outliers: float = 0.05):
        """
            Initializing percentage outliers by parameters needed.
        Args:
            percentage_outliers: the percentage of the outliers across the generated data.
        """
        if 0 <= percentage_outliers <= 1:
            self.percentage_outliers = percentage_outliers
        else:
            raise ValueError("OutliersByPercentage: Percentage value should be of range [0, 1]")

    def transform(self, data_component_values) -> np.ndarray:
        num_outliers = int(len(data_component_values) * self.percentage_outliers)
        outlier_indices = np.random.choice(len(data_component_values), num_outliers, replace=False)

        data_with_outliers = data_component_values.copy()
        outliers = np.random.uniform(-1, 1, num_outliers)
        anomaly_mask = np.zeros(len(data_with_outliers), dtype=bool)

        if len(outliers) > 0:
            data_with_outliers[outlier_indices] = outliers
            anomaly_mask[outlier_indices] = True

        return data_with_outliers
