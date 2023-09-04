import numpy as np

from time_series_components_generator.irregularity_components.noise.noise import Noise


class LinearNoise(Noise):
    """
        A class for generating linear noise.
    """
    def __init__(self, data_component_values: np.ndarray, percentage_of_magnitude: float):
        """
            Initializing linear outliers by parameters needed.
        Args:
            data_component_values: the data component after constructing seasonality, cyclicity, and trend across time intervals.
            percentage_of_magnitude: the percentage of the noise from the generated data.
        """
        super().__init__(data_component_values)
        if 0 <= percentage_of_magnitude <= 1:
            self.percentage_of_magnitude = percentage_of_magnitude
        else:
            raise ValueError("LinearNoise: Percentage value should be of range [0, 1]")

    def generate_noise(self) -> np.ndarray:
        """
            Generate time series data by generating noise by percentage from the data magnitude.

        Returns:
            numpy.ndarray: A numpy array including the data after adding the noise.
        """
        noise_values = np.zeros_like(self.data_component_values)
        for i in range(len(self.data_component_values)):
            noise_values[i] = np.random.normal(0, abs(self.data_component_values[i]) * self.percentage_of_magnitude)
        return self.data_component_values + noise_values
