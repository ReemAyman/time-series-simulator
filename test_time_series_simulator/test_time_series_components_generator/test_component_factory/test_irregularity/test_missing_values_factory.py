import unittest

import numpy as np

from time_series_components_generator.component_factory.irregularity.irregularity_component_factory import \
    IrregularityComponentFactory
from time_series_components_generator.component_factory.irregularity.missing_values_factory import MissingValuesFactory
from time_series_components_generator.irregularity_components.missing_values.missing_values_by_percentage import \
    MissingValuesByPercentage


class TestMissingValuesFactory(unittest.TestCase):
    def setUp(self) -> None:
        time_series_data = np.array([-0.7188723889039199, -1.1109419085035253, 0.4321355614970821, 0.7200556077515603])
        missing_values_parameters = {"percentage": 0.1}
        self.missing_values_factory = MissingValuesFactory(time_series_data, missing_values_parameters)
        self.missing_values_dict = self.missing_values_factory.generate_components()

    def test_missing_values_factory_creation_success(self):
        self.assertIsInstance(self.missing_values_factory, IrregularityComponentFactory)

    def test_missing_value_generate_components_percentage_exist(self):
        self.assertTrue(self.missing_values_dict.__contains__("percentage"))

    def test_missing_value_generate_components_percentage_created_success(self):
        self.assertIsInstance(self.missing_values_dict["percentage"], MissingValuesByPercentage)


if __name__ == '__main__':
    unittest.main()
