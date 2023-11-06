from abc import ABC, abstractmethod

from time_series_data_consumer.consumer.time_series_data_consumer import TimeSeriesDataConsumer


class ConsumerBuilderInterface(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs) -> TimeSeriesDataConsumer:
        pass
