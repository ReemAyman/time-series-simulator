from abc import ABC


class ProducerSerializer(ABC):
    """
    A class for serializing the producer data.
    """
    def __init__(self, serializable):
        self.serializable = serializable

    def serialize(self):
        """
        Serializing the producer data.
        Returns:
            Serialized data.
        """
        pass
