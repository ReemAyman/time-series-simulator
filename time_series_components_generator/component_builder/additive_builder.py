from datetime import datetime

from numpy import ndarray

from time_series_components_generator.component_builder.component_builder import BuilderInterface
from time_series_components_generator.component_factory.interactive.seasonality_factory import SeasonalityFactory
from time_series_components_generator.data_type_enum import DataTypeEnum
from time_series_components_generator.interactive_components.cyclicity import Cyclicity
from time_series_components_generator.interactive_components.trend.linear_trend import LinearTrend
from time_series_components_generator.time_intervals.time_series_generator import TimeSeriesGenerator
from time_series_components_generator.trasformers.noise.linear_noise import LinearNoise
from time_series_components_generator.trasformers.normalizer import MinMaxScalerTransformer
from time_series_components_generator.trasformers.transformer import Transformer


class AdditiveBuilderInterface(BuilderInterface):
    def __init__(self, start_date: datetime, end_date: datetime, freq: str):
        self.start_date = start_date
        self.end_date = end_date
        self.freq = freq
        self._end_product = TimeSeriesGenerator(self.start_date, self.end_date, self.freq, DataTypeEnum.ADDITIVE)

    def set_trend(self, coefficients: ndarray):
        trend = LinearTrend(self._end_product.time_interval_data, coefficients).generate_data_component()
        self._end_product.trend = trend

    def set_seasonality(self, seasonality: str, amplitude: float, multiplier: float, phase_shift: float):
        seasonality_factory = SeasonalityFactory(seasonality, self._end_product.time_interval_data, amplitude, multiplier, phase_shift)
        seasonality_comp = seasonality_factory.generate_components().generate_data_component()
        self._end_product.seasonality_comp = seasonality_comp

    def set_normalizer(self, normalizer: Transformer):
        self._normalizer = normalizer

    def set_noise(self, noise_level: float):
        self._noise = LinearNoise(noise_level)

    def set_cycles(self, amplitude: float, cycle_period: float):
        cycle = Cyclicity(self._end_product.time_interval_data, amplitude, cycle_period).generate_data_component()
        self._end_product.cycle = cycle

    def _generate_dataset(self):
        output = self._end_product.trend + self._end_product.seasonality_comp + self._end_product.cycle
        if hasattr(self, "_normalizer"):
            self.set_normalizer(MinMaxScalerTransformer())
            output = self._normalizer.transform(output)
        # ADD NOISE after normalisation
        output += self._noise.transform(output)
        return output

    @property
    def product(self):
        self._end_product.dataset_values = self._generate_dataset()
        return self._end_product
