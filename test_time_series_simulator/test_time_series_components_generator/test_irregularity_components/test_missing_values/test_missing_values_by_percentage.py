import unittest

import numpy as np

from time_series_components_generator.irregularity_components.missing_values.missing_values_by_percentage import \
    MissingValuesByPercentage


class TestMissingValuesByPercentage(unittest.TestCase):

    def setUp(self) -> None:
        self.data_component_values = np.array([-0.7188723889039199, -1.1109419085035253, 0.4321355614970821, 0.7200556077515603])

    def test_missing_values_by_percentage_valid_percentage_success(self):
        percentage_missing = 0.25
        missing_values_by_percentage = MissingValuesByPercentage(self.data_component_values, percentage_missing)
        self.assertIsInstance(missing_values_by_percentage, MissingValuesByPercentage)

    def test_missing_values_by_percentage_invalid_percentage_less_than_zero_failure(self):
        percentage_missing = -0.25
        self.assertRaises(ValueError, MissingValuesByPercentage, self.data_component_values, percentage_missing)

    def test_missing_values_by_percentage_invalid_percentage_more_than_one_failure(self):
        percentage_missing = 1.25
        self.assertRaises(ValueError, MissingValuesByPercentage, self.data_component_values, percentage_missing)

    def test_generate_missing_values_success(self):
        percentage_missing = 0.25
        missing_values_by_percentage = MissingValuesByPercentage(self.data_component_values, percentage_missing)
        data_with_missing_val = missing_values_by_percentage.generate_missing_values()
        self.assertEqual(np.array(data_with_missing_val is None).size, 1)


if __name__ == '__main__':
    unittest.main()
