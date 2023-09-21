from time_series_data_producer.builder.producer_builder import ProducerBuilderInterface
from time_series_data_producer.producer.time_series_data_producer import TimeSeriesDataProducer


class ProducerFactory:
    """
    A factory class for creating producers using registered builders.

    This class allows you to register builder functions for creating specific
    types of producers and then create instances of those producers using the
    registered builders.

    Note :
    ** Builders here are used to build objects that have different initiation methods instead of using if else conditions in the
    factory class

    Attributes:
    - _builders (dict): A dictionary that maps keys to builder functions.
    """

    def __init__(self):
        """
        Initialize a ProducerFactory instance.

        Initializes the ProducerFactory with an empty dictionary for storing
        registered builders.
        """
        self._builders = {}

    def register_builder(self, key: str, builder: ProducerBuilderInterface):
        """
        Register a builder class for creating a specific type of producer.

        Parameters:
        - key (str): A key that identifies the type of producer to create.
        - builder (callable): A builder function that creates instances of the
          specified type of producer.

        """
        self._builders[key] = builder

    def create(self, key, **kwargs) -> TimeSeriesDataProducer:
        """
        Create an instance of a producer using a registered builder.

        Parameters:
        - key (str): A key that identifies the type of producer to create.
        - **kwargs: Additional keyword arguments to pass to the builder function.

        Returns:
        - object: An instance of the specified type of producer created by the
          registered builder.

        """
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(f"Builder not found for key: {key}")
        return builder
