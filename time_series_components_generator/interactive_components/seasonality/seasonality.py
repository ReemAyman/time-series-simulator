from abc import ABC

from time_series_components_generator.interactive_components.time_series_components import TimeSeriesComponent


class Seasonality(TimeSeriesComponent, ABC):
    """
        Abstract class for seasonality.
    """

