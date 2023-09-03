from abc import ABC, abstractmethod
import numpy as np


class Outliers(ABC):
    """Abstract class for outliers in data."""

    def __init__(self, data_component_values: np.ndarray):
        """
        Initializing outliers for time series data.
        Args:
            data_component_values: the data component after constructing seasonality, cyclicity, and trend across time intervals.
        """
        self.data_component_values = data_component_values

    @abstractmethod
    def generate_outliers(self) -> np.ndarray:
        pass
