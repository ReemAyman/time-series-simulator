import unittest

import numpy as np

from time_series_components_generator.trasformers.outliers_by_percentage import \
    OutlierTransformer


class TestOutliersByPercentage(unittest.TestCase):

    def setUp(self) -> None:
        self.data_component_values = np.array([-0.7188723889039199, -1.1109419085035253, 0.4321355614970821, 0.7200556077515603])

    def test_outliers_by_percentage_valid_percentage_success(self):
        percentage_outliers = 0.25
        outliers_by_percentage = OutlierTransformer(self.data_component_values, percentage_outliers)
        self.assertIsInstance(outliers_by_percentage, OutlierTransformer)

    def test_outliers_by_percentage_invalid_percentage_less_than_zero_failure(self):
        percentage_outliers = -0.25
        self.assertRaises(ValueError, OutlierTransformer, self.data_component_values, percentage_outliers)

    def test_outliers_by_percentage_invalid_percentage_more_than_one_failure(self):
        percentage_outliers = 1.25
        self.assertRaises(ValueError, OutlierTransformer, self.data_component_values, percentage_outliers)

    def test_generate_outliers_success(self):
        percentage_outliers = 0.25
        outliers_by_percentage = OutlierTransformer(self.data_component_values, percentage_outliers)
        data_with_outliers = outliers_by_percentage.generate_outliers()
        subtraction_original_gen = np.abs(data_with_outliers - self.data_component_values)
        self.assertEqual(subtraction_original_gen[subtraction_original_gen > 0].size, 1)


if __name__ == '__main__':
    unittest.main()
