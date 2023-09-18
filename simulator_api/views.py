from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, get_object_or_404

from simulator_api.models import SimulationData, DatasetConfiguration
from simulator_api.serializers import SimulationDataSerializer, DatasetConfigurationSerializer


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


class UpdateSimulator(UpdateAPIView):
    """
        Updating a simulator view [PATCH].
    """
    serializer_class = DatasetConfigurationSerializer
    queryset = DatasetConfiguration.objects.all()
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
