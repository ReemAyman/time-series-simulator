from time_series_data_consumer.builder.consumer_builder import ConsumerBuilderInterface
from time_series_data_consumer.consumer.time_series_data_consumer import TimeSeriesDataConsumer


class ConsumerFactory:
    """
    A factory class for creating consumers using registered builders.

    This class allows you to register builder functions for creating specific
    types of consumers and then create instances of those consumers using the
    registered builders.

    Note :
    ** Builders here are used to build objects that have different initiation methods instead of using if else conditions in the
    factory class

    Attributes:
    - _builders (dict): A dictionary that maps keys to builder functions.
    """

    def __init__(self):
        """
        Initialize a ConsumerFactory instance.

        Initializes the ConsumerFactory with an empty dictionary for storing
        registered builders.
        """
        self._builders = {}

    def register_builder(self, key: str, builder: ConsumerBuilderInterface):
        """
        Register a builder class for creating a specific type of consumer.

        Parameters:
        - key (str): A key that identifies the type of consumers to create.
        - builder (callable): A builder function that creates instances of the
          specified type of consumer.

        """
        self._builders[key] = builder

    def create(self, key, **kwargs) -> TimeSeriesDataConsumer:
        """
        Create an instance of a consumer using a registered builder.

        Parameters:
        - key (str): A key that identifies the type of consumer to create.
        - **kwargs: Additional keyword arguments to pass to the builder function.

        Returns:
        - object: An instance of the specified type of consumer created by the
          registered builder.

        """
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(f"Builder not found for key: {key}")
        return builder
