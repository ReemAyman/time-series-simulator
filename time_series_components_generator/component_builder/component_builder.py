from abc import ABC, abstractmethod


class BuilderInterface(ABC):

    @property
    @abstractmethod
    def product(self):
        pass
