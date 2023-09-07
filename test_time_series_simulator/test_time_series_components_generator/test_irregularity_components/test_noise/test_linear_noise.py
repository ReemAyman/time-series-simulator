import unittest

import numpy as np

from time_series_components_generator.irregularity_components.noise.linear_noise import LinearNoise


class TestLinearNoiseByPercentage(unittest.TestCase):

    def setUp(self) -> None:
        self.data_component_values = np.array([-0.7188723889039199, -1.1109419085035253, 0.4321355614970821, 0.7200556077515603])

    def test_linear_noise_valid_percentage_success(self):
        percentage_of_magnitude = 0.25
        noise_by_percentage = LinearNoise(self.data_component_values, percentage_of_magnitude)
        self.assertIsInstance(noise_by_percentage, LinearNoise)

    def test_noise_invalid_percentage_less_than_zero_failure(self):
        percentage_of_magnitude = -0.25
        self.assertRaises(ValueError, LinearNoise, self.data_component_values, percentage_of_magnitude)

    def test_noise_invalid_percentage_more_than_one_failure(self):
        percentage_of_magnitude = 1.25
        self.assertRaises(ValueError, LinearNoise, self.data_component_values, percentage_of_magnitude)

    def test_generate_noise_success(self):
        percentage_of_magnitude = 0.25
        noise_by_percentage = LinearNoise(self.data_component_values, percentage_of_magnitude)
        noise_values = noise_by_percentage.generate_noise()
        max_noise_values = percentage_of_magnitude * self.data_component_values
        self.assertTrue(noise_values.all() <= max_noise_values.all())


if __name__ == '__main__':
    unittest.main()
