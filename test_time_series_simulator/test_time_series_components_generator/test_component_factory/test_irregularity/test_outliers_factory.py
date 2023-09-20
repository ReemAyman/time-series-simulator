import unittest

import numpy as np

from time_series_components_generator.component_factory.irregularity.irregularity_component_factory import \
    IrregularityComponentFactory
from time_series_components_generator.component_factory.irregularity.outliers_factory import OutliersFactory
from time_series_components_generator.trasformers.outliers_by_percentage import \
    OutlierTransformer


class TestOutliersFactory(unittest.TestCase):
    def setUp(self) -> None:
        time_series_data = np.array([-0.7188723889039199, -1.1109419085035253, 0.4321355614970821, 0.7200556077515603])
        outliers_parameters = {"percentage": 0.1}
        self.outliers_factory = OutliersFactory(time_series_data, outliers_parameters)
        self.outliers_dict = self.outliers_factory.generate_components()

    def test_outliers_factory_creation_success(self):
        self.assertIsInstance(self.outliers_factory, IrregularityComponentFactory)

    def test_missing_value_generate_components_percentage_exist(self):
        self.assertTrue(self.outliers_dict.__contains__("percentage"))

    def test_missing_value_generate_components_percentage_created_success(self):
        self.assertIsInstance(self.outliers_dict["percentage"], OutlierTransformer)


if __name__ == '__main__':
    unittest.main()
