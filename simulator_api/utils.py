from simulator_api.models import DatasetConfiguration, SimulationData
from time_series_configuration.configuration_facade import ConfigurationFacade
from time_series_configuration.configuration_reader.postgre_configuration_reader import PostgreReader
from time_series_data_consumer.builder.consumer_builder_kafka import KafkaConsumerBuilder
from time_series_data_consumer.consumer.time_series_data_consumer_kafka import TimeSeriesDataConsumerKafka
from time_series_data_consumer.consumer_factory import ConsumerFactory
from time_series_data_producer.builder.producer_builder_csv import CsvProducerBuilder
from time_series_data_producer.builder.producer_builder_kafka import KafkaProducerBuilder
from time_series_data_producer.producer_factory import ProducerFactory
from time_series_director.time_series_director import TimeSeriesDirector


def run_simulator(simulator_config, data_producer, simulator_id):
    """
        Get the data from the response to encode it to input to configure.
    Args:
        simulator_id: simulator id.
        data_producer: data producer type.
        simulator_config: the simulator configuration data.
    Returns:
        TimeSeriesDirector: the director that runs and generates the time series data.
    """
    datasets_ids = DatasetConfiguration.objects.filter(
        simulation_data_id=simulator_id).values_list('id', flat=True)

    datasets = simulator_config["datasets"]
    list_of_configurators = []

    for dataset in datasets:
        config_data = dict()
        config_data["start_date"] = simulator_config["start_date"]
        config_data["end_date"] = simulator_config["end_date"]
        config_data["data_type"] = simulator_config["type"]
        config_data["frequency"] = dataset["frequency"]
        config_data["trend_coefficients"] = dataset["trend_coefficients"]
        config_data["missing_percentage"] = dataset["missing_percentage"]
        config_data["outlier_percentage"] = dataset["outlier_percentage"]
        config_data["noise_level"] = dataset["noise_level"]
        config_data["cycle_amplitude"] = dataset["cycle_amplitude"]
        config_data["cycle_frequency"] = dataset["cycle_frequency"]
        config_data["seasonality_components"] = dataset["seasonality_components"]
        config_data["generator_id"] = dataset["generator_id"]
        config_data["feature_id"] = dataset["feature_id"]
        list_of_configurators.append(ConfigurationFacade(PostgreReader(config_data)))

    simulator_director = TimeSeriesDirector(list_of_configurators)

    # Building the datasets according to the producer type.
    for i, dataset in enumerate(simulator_director.build()):
        producer_factory = ProducerFactory()
        if data_producer == 'csv':
            csv_producer_builder = CsvProducerBuilder()
            producer_factory.register_builder("csv", csv_producer_builder(generated_data=dataset, location=f"generated_datasets/test_dataset_{i}.csv"))
            producer = producer_factory.create("csv",
                                               location=f"generated_datasets/test_dataset_{i}.csv")
            producer.store_data()
        else:
            kafka_producer_builder = KafkaProducerBuilder()
            producer_factory.register_builder("kafka", kafka_producer_builder(generated_data=dataset, topic=simulator_config["sink_id"],
                                                                              generator_id=list_of_configurators[i].generator_id, feature_id=list_of_configurators[i].feature_id))
            producer = producer_factory.create("kafka", topic=simulator_config["sink_id"],
                                               generator_id=list_of_configurators[i].generator_id, feature_id=list_of_configurators[i].feature_id)

            consumer_factory = ConsumerFactory()
            kafka_consumer_builder = KafkaConsumerBuilder()
            consumer_factory.register_builder("kafka", kafka_consumer_builder(topic=simulator_config["sink_id"], data_count=dataset.shape[0]))
            consumer = consumer_factory.create("kafka", topic=simulator_config["sink_id"], data_count=dataset.shape[0])

            producer.store_data()
            consumer.consume_data()
