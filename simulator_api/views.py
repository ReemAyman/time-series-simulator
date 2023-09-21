from threading import Thread

from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, get_object_or_404
from rest_framework.response import Response

from simulator_api.models import SimulationData, DatasetConfiguration
from simulator_api.serializers import SimulationDataSerializer
from time_series_configuration.configuration_facade import ConfigurationFacade
from time_series_configuration.configuration_reader.postgre_configuration_reader import PostgreReader
from time_series_data_producer.builder.producer_builder_csv import CsvProducerBuilder
from time_series_data_producer.producer_factory import ProducerFactory
from time_series_director.time_series_director import TimeSeriesDirector

# Global variable for the thread
simulator_thread = Thread()


class SimulatorRunner(Thread):
    """
        A thread for create, run, and stop the simulator (connected to the end points to the user requests).
    """
    def __init__(self, simulator_config=None):
        Thread.__init__(self)
        # A flag parameter for stopping the process.
        self.kill_process = False
        self.data_producer = "csv"

        self.simulator_director = self.get_data(simulator_config)
        self.use_case_name = simulator_config["use_case_name"]

        self.datasets_ids = DatasetConfiguration.objects.filter(
            simulation_data_id=SimulationData.objects.get(use_case_name=self.use_case_name).id).values_list('id', flat=True)

        # A flag parameter for starting the process.
        self.process_started = False

    def run(self) -> None:
        print(f"SimulatorRunner process initialized with process id {self.ident} ...")

        # Saving the data producer type and process id
        SimulationData.objects.filter(use_case_name=self.use_case_name).update(process_id=self.ident)

        while True:
            if self.process_started:
                print(f"SimulatorRunner process started with process id {self.ident} ...")
                curr_index = 0
                while not self.kill_process:
                    # Building the datasets according to the producer type.
                    for i, dataset in enumerate(self.simulator_director.build()):
                        producer_factory = ProducerFactory()
                        if self.data_producer == 'csv':
                            csv_producer_builder = CsvProducerBuilder()
                            producer_factory.register_builder("csv", csv_producer_builder(generated_data=dataset,
                                                                                          location=f"generated_datasets/test_dataset_{i}.csv"))
                            producer = producer_factory.create("csv", location=f"generated_datasets/test_dataset_{i}.csv")
                            producer.store_data()
                            DatasetConfiguration.objects.filter(id=self.datasets_ids[i]).update(producing_status="Succeeded")
                            curr_index = i

                if self.kill_process:
                    print(f"SimulatorRunner process stopped with process id {self.ident} ...")
                    self.process_started = False
                    if curr_index >= len(self.datasets_ids):
                        DatasetConfiguration.objects.filter(id__in=self.datasets_ids[curr_index:]).update(producing_status="Failed")
                SimulationData.objects.filter(process_id=self.ident).update(process_id=-1)

    def get_data(self, simulator_config):
        """
            Get the data from the response to encode it to input to configure.
        Args:
            simulator_config: the simulator configuration data.
        Returns:
            TimeSeriesDirector: the director that runs and generates the time series data.
        """
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
            list_of_configurators.append(ConfigurationFacade(PostgreReader(config_data)))

        # Initiate the director class to start building time series dataset
        return TimeSeriesDirector(list_of_configurators)


class CreateSimulator(CreateAPIView):
    """
        Creating a simulator view [POST].
    """
    serializer_class = SimulationDataSerializer

    def create(self, request, *args, **kwargs):
        simulator_serialized = SimulationDataSerializer(data=request.data)
        if simulator_serialized.is_valid():
            simulator_serialized.save()
        global simulator_thread
        simulator_thread = SimulatorRunner(simulator_config=simulator_serialized.data)
        simulator_thread.deamon = False
        simulator_thread.start()
        return Response(simulator_serialized.data)


class ListSimulator(ListAPIView):
    """
        Listing all simulators view [GET].
    """
    serializer_class = SimulationDataSerializer
    queryset = SimulationData.objects.all()


class RunSimulator(UpdateAPIView):
    """
        Running a simulator view [PATCH].
    """
    serializer_class = SimulationDataSerializer
    queryset = SimulationData.objects.all()
    lookup_field = 'process_id'

    def get_object(self):
        """
            Overriding 'get_object' to get the correct object according to the lookup filter.
        Returns:
            the object after using the filter [which is the instance in the serializer in the 'update' method].
        """
        queryset = self.get_queryset()
        filters = dict()
        filters[self.lookup_field] = self.request.data[self.lookup_field]

        obj = get_object_or_404(queryset, **filters)
        self.check_object_permissions(self.request, obj)
        return obj

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.datasets.all().update(producing_status="Running")
        simulator_thread.process_started = True
        return Response(SimulationDataSerializer(instance).data)


class StopSimulator(UpdateAPIView):
    """
        Stopping a simulator view [PATCH].
    """
    serializer_class = SimulationDataSerializer
    queryset = SimulationData.objects.all()
    lookup_field = 'process_id'

    def get_object(self):
        """
            Overriding 'get_object' to get the correct object according to the lookup filter.
        Returns:
            the object after using the filter [which is the instance in the serializer in the 'update' method].
        """
        queryset = self.get_queryset()
        filters = dict()
        filters[self.lookup_field] = self.request.data[self.lookup_field]

        obj = get_object_or_404(queryset, **filters)
        self.check_object_permissions(self.request, obj)
        return obj

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.datasets.all().update(producing_status="Failed")
        if simulator_thread is not None:
            simulator_thread.kill_process = True
        return Response(SimulationDataSerializer(instance).data)
