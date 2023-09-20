import random

import pandas as pd

from time_series_configuration.configuration_facade import ConfigurationFacade
from time_series_configuration.configuration_reader.yaml_configuration_reader import YamlReader
from time_series_data_producer.builder.producer_builder_csv import CsvProducerBuilder
from time_series_data_producer.producer_factory import ProducerFactory
from time_series_director.time_series_director import TimeSeriesDirector

random.seed(22)


# def generate_dataset_from_config() -> None:
#     """
#         Generate datasets from configurations and saving into the targeted source.
#     """
#     # Reading the data configuration from a YAML file
#     # -------------------------------------------------------
#     yaml_file_reader = YamlReader('data_config.yaml')
#     init_data = yaml_file_reader.read_data()
#     # -------------------------------------------------------
#     datasets_number = init_data["datasets_number"]
#
#     data_time_intervals = TimeSeriesGenerator(init_data["start_date"], init_data["end_date"],
#                                               init_data["frequency"]).generate_time_interval()
#     seasonalities = SeasonalityFactory(data_time_intervals).generate_components()
#     trends = TrendFactory(time_intervals=data_time_intervals, trend_parameters=init_data["trend"]).generate_components()
#     curr_seasonality = init_data["seasonality"]
#     curr_trend = init_data["trend"]
#     # --------------------------------------------------------------
#     # Iterating over the number of datasets generated
#     for dataset_count in range(datasets_number):
#         for seasonality in curr_seasonality:
#             for trend in curr_trend.keys():
#
#                 # Generate seasonality and trend
#                 seasonality_component = seasonalities[seasonality].generate_data_component()
#                 trend_component = trends[trend].generate_data_component()
#
#                 # Operate on the generated components according to data type
#                 total_component = pd.Series()
#                 if init_data["data_type"] == "Additive":
#                     seasonality_component += np.ones(len(data_time_intervals))
#                     trend_component += np.ones(len(data_time_intervals))
#                     total_component = seasonality_component + trend_component
#                 else:
#                     total_component = seasonality_component * trend_component
#
#                 # Rescale generated data to range (-1, 1)
#                 scaler = MinMaxScaler(feature_range=(-1, 1))
#                 data_series_values = scaler.fit_transform(total_component.values.reshape(-1, 1))
#
#                 # Generate noise, outliers and missing data
#                 noises = NoiseFactory(data_series_values, init_data["noise"]).generate_components()
#                 data_series_values = noises[list(init_data["noise"].keys())[0]].generate_noise()
#
#                 outliers = OutliersFactory(data_series_values, init_data["outlier"]).generate_components()
#                 data_series_values = outliers[list(init_data["outlier"].keys())[0]].generate_outliers()
#
#                 missing_values = MissingValuesFactory(data_series_values, init_data["missing"]).generate_components()
#                 data_series_values = missing_values[list(init_data["missing"].keys())[0]].generate_missing_values()
#
#                 # Save data into csv file
#                 TimeSeriesDataProducerCSV(data_series_values, str(dataset_count)).store_data()


def main():
    configuration_files_locations = ["config_files/data_config.yaml"]
    list_of_configurators = []
    for file_location in configuration_files_locations:
        list_of_configurators.append(ConfigurationFacade(YamlReader(file_location)))

    # Initiate the director class to start building time series dataset
    d = TimeSeriesDirector(list_of_configurators)
    for i, dataset in enumerate(d.build()):
        producer_factory = ProducerFactory()
        csv_producer_builder = CsvProducerBuilder()
        producer_factory.register_builder("csv", csv_producer_builder(generated_data=dataset, location=f"generated_datasets/test_dataset_{i}.csv"))
        producer = producer_factory.create("csv", location=f"generated_datasets/test_dataset_{i}.csv")
        producer.store_data()


if __name__ == "__main__":
    main()
