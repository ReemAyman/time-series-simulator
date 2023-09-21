from abc import ABC, abstractmethod

from time_series_data_producer.producer.time_series_data_producer import TimeSeriesDataProducer


class ProducerBuilderInterface(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs) -> TimeSeriesDataProducer:
        pass
