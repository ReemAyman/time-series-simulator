import graphene

from graphene_django import DjangoObjectType
from simulator_api.models import SimulationData, DatasetConfiguration, SeasonalityModel


class SimulatorType(DjangoObjectType):
    """
    A simulator class used for a simulator output of the mutation.
    """
    class Meta:
        model = SimulationData
        fields = "__all__"


class DatasetType(DjangoObjectType):
    """
    A dataset class used for a dataset configuration output of the mutation.
    """
    class Meta:
        model = DatasetConfiguration
        fields = "__all__"


class SeasonalityType(DjangoObjectType):
    """
    A seasonality class used for a seasonality component output of the mutation.
    """
    class Meta:
        model = SeasonalityModel
        fields = "__all__"


class SimulatorInputType(graphene.InputObjectType):
    """
    A simulator input class used for adding a simulator input to the mutation.
    """
    start_date = graphene.DateTime(required=True)
    end_date = graphene.DateTime(required=True)
    data_type = graphene.String(required=True)
    use_case_name = graphene.String(required=True)
    producer_type = graphene.String()
    sink_id = graphene.String()


class DatasetInputType(graphene.InputObjectType):
    """
    A dataset input class used for adding a dataset configuration input to the mutation.
    """
    simulator_id = graphene.ID(required=True)
    frequency = graphene.String(required=True)
    trend_coefficients = graphene.List(graphene.Int, required=True)
    missing_percentage = graphene.Float(required=True)
    outlier_percentage = graphene.Float(required=True)
    noise_level = graphene.Int(required=True)
    cycle_amplitude = graphene.Int(required=True)
    cycle_frequency = graphene.Int(required=True)
    generator_id = graphene.String()
    feature_id = graphene.String()


class SeasonalityInputType(graphene.InputObjectType):
    """
    A seasonality input class used for adding a seasonality component input to the mutation.
    """
    dataset_id = graphene.ID(required=True)
    frequency = graphene.String(required=True)
    multiplier = graphene.Int(required=True)
    phase_shift = graphene.Int(required=True)
    amplitude = graphene.Int(required=True)


class CreateSimulator(graphene.Mutation):
    """
    A mutation for creating a simulator.
    """
    class Arguments:
        simulator_data = SimulatorInputType(required=True)

    simulator = graphene.Field(SimulatorType)

    @staticmethod
    def mutate(root, info, simulator_data):
        simulator_instance = SimulationData(
            start_date=simulator_data.start_date,
            end_date=simulator_data.end_date,
            type=simulator_data.data_type,
            use_case_name=simulator_data.use_case_name,
            producer_type=simulator_data.producer_type,
            sink_id=simulator_data.sink_id
        )
        simulator_instance.save()
        return CreateSimulator(simulator=simulator_instance)


class CreateDataset(graphene.Mutation):
    """
    A mutation for creating a dataset.
    """
    class Arguments:
        dataset_data = DatasetInputType(required=True)

    dataset = graphene.Field(DatasetType)

    @staticmethod
    def mutate(root, info, dataset_data):
        dataset_instance = DatasetConfiguration(
            simulation_data=SimulationData.objects.get(pk=dataset_data.simulator_id),
            frequency=dataset_data.frequency,
            trend_coefficients=dataset_data.trend_coefficients,
            missing_percentage=dataset_data.missing_percentage,
            outlier_percentage=dataset_data.outlier_percentage,
            noise_level=dataset_data.noise_level,
            cycle_amplitude=dataset_data.cycle_amplitude,
            cycle_frequency=dataset_data.cycle_frequency,
            generator_id=dataset_data.generator_id,
            feature_id=dataset_data.feature_id
        )
        dataset_instance.save()
        return CreateDataset(dataset=dataset_instance)


class CreateSeasonality(graphene.Mutation):
    """
    A mutation for creating a seasonality component.
    """
    class Arguments:
        seasonality_data = SeasonalityInputType(required=True)

    seasonality = graphene.Field(SeasonalityType)

    @staticmethod
    def mutate(root, info, seasonality_data):
        seasonality_instance = SeasonalityModel(
            dataset_config=DatasetConfiguration.objects.get(pk=seasonality_data.dataset_id),
            frequency=seasonality_data.frequency,
            multiplier=seasonality_data.multiplier,
            phase_shift=seasonality_data.phase_shift,
            amplitude=seasonality_data.amplitude
        )
        seasonality_instance.save()
        return CreateSeasonality(seasonality=seasonality_instance)


class Query(graphene.ObjectType):
    """
    A query class for adding all queries needed.
    """
    all_simulators = graphene.List(SimulatorType)
    simulator = graphene.Field(SimulatorType, use_case_name=graphene.String())

    def resolve_all_simulators(self, info, **kwargs):
        return SimulationData.objects.all()

    def resolve_simulator(self, info, use_case_name):
        return SimulationData.objects.get(use_case_name=use_case_name)


class Mutation(graphene.ObjectType):
    """
    A mutation class for adding all mutations needed.
    """
    create_simulator = CreateSimulator.Field()
    create_dataset = CreateDataset.Field()
    create_seasonality = CreateSeasonality.Field()


# Adding the queries and mutations to the schema.
schema = graphene.Schema(query=Query, mutation=Mutation)

