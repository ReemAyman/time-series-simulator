from threading import Thread

from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, get_object_or_404
from rest_framework.response import Response

from simulator_api.models import SimulationData, DatasetConfiguration
from simulator_api.serializers import SimulationDataSerializer, DatasetConfigurationSerializer


class SimulatorRunner(Thread):
    def __init__(self, simulator_config):
        self.simulator_config = simulator_config
        self.kill_process = False
        Thread.__init__(self)

    def run(self) -> None:
        while not self.kill_process:
            pass


class CreateSimulator(CreateAPIView):
    """
        Creating a simulator view [POST].
    """
    serializer_class = SimulationDataSerializer


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
    lookup_field = 'id'

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
        return Response(SimulationDataSerializer(instance).data)


class StopSimulator(UpdateAPIView):
    """
        Stopping a simulator view [PATCH].
    """
    serializer_class = SimulationDataSerializer
    queryset = SimulationData.objects.all()
    lookup_field = 'id'

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
        return Response(SimulationDataSerializer(instance).data)
