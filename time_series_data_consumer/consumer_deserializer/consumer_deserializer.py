from abc import ABC


class ConsumerDeserializer(ABC):
    """
    A class for deserializing the consumer data.
    """
    def __init__(self, deserializable):
        self.deserializable = deserializable

    def deserialize(self):
        """
        Deserializing the consumer data.
        Returns:
            Deserialized data.
        """
        pass
