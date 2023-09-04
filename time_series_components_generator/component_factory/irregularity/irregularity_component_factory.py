from abc import ABC

import numpy as np

from time_series_components_generator.component_factory.time_series_component_factory import TimeSeriesComponentFactory


class IrregularityComponentFactory(TimeSeriesComponentFactory, ABC):
    """
        An abstract class for generating irregular time series data (outliers, noise, missing values)
    """

    def __init__(self, series_data_component_values: np.ndarray, component_parameters: dict):
        """
            Initializing irregular component factory.
        Args:
            series_data_component_values: the time series data generated
            component_parameters: the noise parameters read from the source.
        """
        self.series_data_component_values = series_data_component_values
        self.component_parameters = component_parameters
