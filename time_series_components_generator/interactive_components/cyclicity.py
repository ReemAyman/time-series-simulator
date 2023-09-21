import numpy as np
from pandas import Series, DatetimeIndex

from time_series_components_generator.interactive_components.time_series_components import TimeSeriesComponent


class Cyclicity(TimeSeriesComponent):
    """
        A class for time series cyclicity component.
    """

    def __init__(self, time_interval_data: DatetimeIndex, amplitude: float, cycle_period: float):
        """
            Initializing the components of the cyclic component.
        Args:
            time_interval_data: the time intervals initialized by start time, end time, and frequency.
            amplitude: the cyclic amplitude.
            cycle_period: the cyclic period.
        """
        super().__init__(time_interval_data)
        self.amplitude = amplitude
        self.cycle_period = cycle_period

    def generate_data_component(self) -> Series:
        """
            Add cyclicity component to the time series data.

        Returns:
            pandas.Series: The cyclic component of the time series.
        """
        return Series(self.amplitude * np.sin(2 * np.pi * self.time_interval_data.year / self.cycle_period))
