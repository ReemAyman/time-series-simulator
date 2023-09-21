from threading import Thread

from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, get_object_or_404
from rest_framework.response import Response

from simulator_api.models import SimulationData
from simulator_api.serializers import SimulationDataSerializer
from simulator_api.utils import SimulatorRunner


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
