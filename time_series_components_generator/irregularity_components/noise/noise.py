from abc import ABC, abstractmethod
import numpy as np


class Noise(ABC):
    """Abstract class for noise."""

    def __init__(self, data_component_values: np.ndarray):
        """
        Initializing noise component for time series data.
        Args:
            data_component_values: the data component after constructing seasonality, cyclicity, and trend across time intervals.
        """
        self.component_data = data_component_values

    @abstractmethod
    def generate_noise(self) -> np.ndarray:
        pass
