import json

import pandas as pd
import requests

from time_series_components_generator.time_series_builder_factory import TimeSeriesBuilderFactory
from time_series_components_generator.trasformers.missing_values_by_percentage import MissingValuesTransformer
from time_series_components_generator.trasformers.normalizer import MinMaxScalerTransformer
from time_series_components_generator.trasformers.outliers_by_percentage import OutlierTransformer


class TimeSeriesDirector:
    def __init__(self, configuration_readers: list):
        # the director is responsible for building more than one product (one dataset)
        self.configurators = configuration_readers

    def build(self):
        for configurator in self.configurators:
            builder = TimeSeriesBuilderFactory.create(data_type=configurator.data_type,
                                                      start_date=configurator.start_date,
                                                      end_date=configurator.end_date,
                                                      freq=configurator.frequency)
            builder.set_trend(configurator.trend_coefficients)

            for component in configurator.seasonality:
                builder.set_seasonality(component["frequency"], float(component["amplitude"]),
                                        float(component["multiplier"]),
                                        float(component["phase_shift"]))

            builder.set_cycles(configurator.cyclic_amplitude, configurator.cyclic_period)

            normalizer = MinMaxScalerTransformer()

            builder.set_normalizer(normalizer)

            builder.set_noise(configurator.noise_level)

            product = builder.product

            # add  outliers

            data_with_outliers = OutlierTransformer(configurator.percentage_outliers).transform(
                product.dataset_values)

            # add missings
            data_with_missings = MissingValuesTransformer(configurator.missings_percentage).transform(
                data_with_outliers)
            final_dataframe = pd.DataFrame({'value': data_with_missings, 'timestamp': product.time_interval_data})
            # self.store_data_nifi(final_dataframe)
            yield final_dataframe

    @staticmethod
    def store_data_nifi(self, df: pd.DataFrame):
        """
        Store the generated data in database through NiFi.
        """
        df = df.fillna('')
        df['timestamp'] = df['timestamp'].astype(str)

        # POST request call to nifi port
        url = "http://host.docker.internal:5000"
        requests.post(url=url, json={'generated_dataset': df.to_json()},
                      headers={'content-type': 'application/json'})
