from abc import ABC

from pandas import DatetimeIndex

from time_series_components_generator.interactive_components.time_series_components import TimeSeriesComponent


class Seasonality(TimeSeriesComponent, ABC):
    """
        Abstract class for seasonality.
    """
    def __init__(self, time_interval_data: DatetimeIndex, seasonality_multiplier: float,
                 amplitude: float, phase_shift: float = 0):
        super().__init__(time_interval_data)
        self.seasonality_multiplier = seasonality_multiplier
        self.amplitude = amplitude
        self.phase_shift = phase_shift
