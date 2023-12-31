from rest_framework import serializers

from simulator_api.models import SeasonalityModel, DatasetConfiguration, SimulationData


class SeasonalitySerializer(serializers.ModelSerializer):
    """
        A serializer for seasonality model.
    """
    class Meta:
        model = SeasonalityModel
        fields = ('frequency', 'multiplier', 'phase_shift', 'amplitude')


class DatasetConfigurationSerializer(serializers.ModelSerializer):
    """
        A serializer for dataset configuration model.
    """
    seasonality_components = SeasonalitySerializer(many=True)

    class Meta:
        model = DatasetConfiguration
        fields = ('frequency', 'trend_coefficients', 'missing_percentage',
                  'outlier_percentage', 'noise_level', 'cycle_amplitude',
                  'cycle_frequency', 'producing_status', 'seasonality_components',
                  'generator_id', 'feature_id')


class SimulationDataSerializer(serializers.ModelSerializer):
    """
        A serializer for simulation model.
    """
    datasets = DatasetConfigurationSerializer(many=True, partial=True)

    class Meta:
        model = SimulationData
        fields = ('start_date', 'end_date', 'type', 'use_case_name', 'meta_data',
                  'producer_type', 'process_id', 'datasets', 'sink_id')

    def create(self, validated_data):
        """
            Overriding 'create' method when doing POST request for handling nested serializers.
        Args:
            validated_data: the data passed in the request body, serialized, and validated.
        Returns:
            the instance data after nested serialization.
        """
        datasets_data = validated_data.pop('datasets')
        simulation_data = SimulationData.objects.create(**validated_data)

        # Iterating over the nested data and create instance according to its model.
        for dataset_data in datasets_data:
            seasonality_components_data = dataset_data.pop('seasonality_components')
            dataset_config = DatasetConfiguration.objects.create(simulation_data=simulation_data, **dataset_data)

            for seasonality_component_data in seasonality_components_data:
                SeasonalityModel.objects.create(dataset_config=dataset_config, **seasonality_component_data)

        return simulation_data
