import numpy as np

from time_series_components_generator.trasformers.transformer import Transformer


class LinearNoise(Transformer):
    """
        A class for generating linear noise.
    """
    def __init__(self, noise_level: float):
        """
            Initializing linear outliers by parameters needed.
        Args:
            noise_level: the percentage of the noise from the generated data.
        """
        self.noise_level = noise_level

    def transform(self, data_component_values) -> np.ndarray:
        """
            Generate time series data by generating noise by percentage from the data magnitude.

        Args:
            data_component_values:

        Returns:
            numpy.ndarray: A numpy array including the data after adding the noise.
        """
        noise = np.zeros_like(data_component_values)
        for i in range(len(data_component_values)):
            noise[i] = np.random.normal(0, abs(data_component_values[i]) * self.noise_level)\
                if self.noise_level > 0 else 0
        return np.array((data_component_values + noise))
