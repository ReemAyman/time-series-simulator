import numpy as np

from time_series_components_generator.trasformers.transformer import Transformer


class MissingValuesTransformer(Transformer):
    """Class for missing values in data by percentage."""

    def __init__(self, percentage_missing: float = 0.05):
        if 0 <= percentage_missing <= 1:
            self.percentage_missing = percentage_missing
        else:
            raise ValueError("MissingValuesByPercentage: Percentage value should be of range [0, 1]")

    def transform(self, data_component_values) -> np.ndarray:
        num_missing = int(len(data_component_values) * self.percentage_missing)
        missing_indices = np.random.choice(len(data_component_values), size=num_missing, replace=False)

        data_with_missing_val = data_component_values.copy()
        data_with_missing_val[missing_indices] = np.nan

        return data_with_missing_val
