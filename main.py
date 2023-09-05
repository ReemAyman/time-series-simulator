import random

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from time_series_components_generator.component_factory.interactive.seasonality_factory import SeasonalityFactory
from time_series_components_generator.component_factory.interactive.trend_factory import TrendFactory
from time_series_components_generator.component_factory.irregularity.missing_values_factory import MissingValuesFactory
from time_series_components_generator.component_factory.irregularity.noise_factory import NoiseFactory
from time_series_components_generator.component_factory.irregularity.outliers_factory import OutliersFactory
from time_series_components_generator.time_intervals.time_interval_generator import TimeIntervalGenerator
from time_series_configuration.configuration_reader.yaml_configuration_reader import YamlConfigurationReader
from time_series_data_store.time_series_data_store_csv import TimeSeriesDataStoreCSV

random.seed(22)


def generate_dataset_from_config() -> None:
    """
        Generate datasets from configurations and saving into the targeted source.
    """
    # Reading the data configuration from a YAML file
    # -------------------------------------------------------
    yaml_file_reader = YamlConfigurationReader('data_config.yaml')
    init_data = yaml_file_reader.read_data()
    # -------------------------------------------------------
    datasets_number = init_data["datasets_number"]

    data_time_intervals = TimeIntervalGenerator(init_data["start_date"], init_data["end_date"],
                                                init_data["frequency"]).generate_time_interval()
    seasonalities = SeasonalityFactory(data_time_intervals).generate_components()
    trends = TrendFactory(time_intervals=data_time_intervals, trend_parameters=init_data["trend"]).generate_components()
    curr_seasonality = init_data["seasonality"]
    curr_trend = init_data["trend"]
    # --------------------------------------------------------------
    # Iterating over the number of datasets generated
    for dataset_count in range(datasets_number):
        for seasonality in curr_seasonality:
            for trend in curr_trend.keys():

                # Generate seasonality and trend
                seasonality_component = seasonalities[seasonality].generate_data_component()
                trend_component = trends[trend].generate_data_component()

                # Operate on the generated components according to data type
                total_component = pd.Series()
                if init_data["data_type"] == "Additive":
                    seasonality_component += np.ones(len(data_time_intervals))
                    trend_component += np.ones(len(data_time_intervals))
                    total_component = seasonality_component + trend_component
                else:
                    total_component = seasonality_component * trend_component

                # Rescale generated data to range (-1, 1)
                scaler = MinMaxScaler(feature_range=(-1, 1))
                data_series_values = scaler.fit_transform(total_component.values.reshape(-1, 1))

                # Generate noise, outliers and missing data
                noises = NoiseFactory(data_series_values, init_data["noise"]).generate_components()
                data_series_values = noises[list(init_data["noise"].keys())[0]].generate_noise()

                outliers = OutliersFactory(data_series_values, init_data["outlier"]).generate_components()
                data_series_values = outliers[list(init_data["outlier"].keys())[0]].generate_outliers()

                missing_values = MissingValuesFactory(data_series_values, init_data["missing"]).generate_components()
                data_series_values = missing_values[list(init_data["missing"].keys())[0]].generate_missing_values()

                # Save data into csv file
                TimeSeriesDataStoreCSV(data_series_values, data_time_intervals, str(dataset_count)).store_data()


def main():
    generate_dataset_from_config()


if __name__ == "__main__":
    main()
