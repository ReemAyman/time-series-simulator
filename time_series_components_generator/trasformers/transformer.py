from abc import ABC, abstractmethod

import numpy as np


class Transformer(ABC):
    """
        A class for transformers of the time series data after construction.
    """

    @abstractmethod
    def transform(self, data_component_values) -> np.ndarray:
        """
            Transforming the time series data.
        Args:
            data_component_values: the data component after constructing seasonality, cyclicity, and trend across time intervals.

        Returns:
            Time series data after transformation.
        """
        pass
