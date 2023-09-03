import numpy as np

from time_series_components_generator.irregularity_components.noise.noise import Noise


class LinearNoise(Noise):
    def __init__(self, data_component_values: np.ndarray, percentage_of_magnitude:float):
        super().__init__(data_component_values)
        self.percentage_of_magnitude = percentage_of_magnitude

    def generate_noise(self) -> np.ndarray:
        """
        Generate time series data by generating noise by percentage from the data magnitude.

        Returns:
            pandas.Series: The noise component of the time series.
        """
        noise_values = np.zeros_like(self.data_component_values)
        for i in range(len(self.data_component_values)):
            noise_values[i] = np.random.normal(0, abs(self.data_component_values[i]) * self.percentage_of_magnitude)
        return (self.data_component_values + noise_values)[:, 0]
