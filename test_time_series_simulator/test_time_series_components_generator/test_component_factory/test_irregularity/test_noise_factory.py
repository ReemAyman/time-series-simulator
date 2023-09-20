import unittest

import numpy as np

from time_series_components_generator.component_factory.irregularity.irregularity_component_factory import \
    IrregularityComponentFactory
from time_series_components_generator.component_factory.irregularity.noise_factory import NoiseFactory
from time_series_components_generator.trasformers.noise.linear_noise import LinearNoise


class TestNoiseFactory(unittest.TestCase):
    def setUp(self) -> None:
        time_series_data = np.array([-0.7188723889039199, -1.1109419085035253, 0.4321355614970821, 0.7200556077515603])
        noise_parameters = {"percentage": 0.1}
        self.noise_factory = NoiseFactory(time_series_data, noise_parameters)
        self.noise_dict = self.noise_factory.generate_components()

    def test_noise_factory_creation_success(self):
        self.assertIsInstance(self.noise_factory, IrregularityComponentFactory)

    def test_missing_value_generate_components_percentage_exist(self):
        self.assertTrue(self.noise_dict.__contains__("percentage"))

    def test_missing_value_generate_components_percentage_created_success(self):
        self.assertIsInstance(self.noise_dict["percentage"], LinearNoise)


if __name__ == '__main__':
    unittest.main()
