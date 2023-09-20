from datetime import datetime

import numpy as np
import pandas as pd

from time_series_components_generator.data_type_enum import DataTypeEnum


class TimeSeriesGenerator:
    """
    A class for generating time series interval.
    """

    def __init__(self, start_date: datetime, end_date: datetime, frequency: str, data_type: DataTypeEnum):
        """
        Initializing time series interval instance by start time and frequency.

        Args:
            start_date: the start date of the time interval.
            end_date: the end date of the time interval.
            frequency: the sampling frequency of the time points in the time interval.
        """
        self._start_date = start_date
        self._end_date = end_date
        self._frequency = frequency
        self._time_interval_data = self._generate_time_interval()
        self._data_type = data_type

    def _generate_time_interval(self) -> pd.DatetimeIndex:
        """
        Generate time interval of the time series data.

        Returns:
            pandas.DatetimeIndex: The generated time index.
        """
        date_interval = pd.date_range(start=self._start_date, end=self._end_date, freq=self._frequency)
        return date_interval

    # @property
    # def time_interval_data(self):
    #     return self._time_interval_data

    @property
    def trend(self):
        if hasattr(self, "_trend"):
            return self._trend
        elif self._data_type == DataTypeEnum.ADDITIVE.value:
            return np.zeros(len(self._time_interval_data))

    @trend.setter
    def trend(self, value):
        self._trend = value

    @property
    def seasonality(self):
        if hasattr(self, "_seasonality"):
            return self._seasonality
        elif self._data_type == DataTypeEnum.ADDITIVE.value:
            return np.zeros(len(self._time_interval_data))

    @seasonality.setter
    def seasonality(self, seasonality_series):
        if self._data_type == DataTypeEnum.ADDITIVE.value:
            self._seasonality = self.seasonality + seasonality_series
        elif self._data_type == DataTypeEnum.MULTIPLICATIVE.value:
            self._seasonality = self.seasonality * seasonality_series

    # @property
    # def noise(self):
    #     if hasattr(self, "_noise"):
    #         return self._noise
    #     elif self._data_type == DataTypeEnum.ADDITIVE.value:
    #         return np.zeros(self.time_series_index.shape)
    #
    # @noise.setter
    # def noise(self, value):
    #     self._noise = value

    @property
    def cycle(self):
        if hasattr(self, "_cycle"):
            return self._cycle
        elif self._data_type == DataTypeEnum.ADDITIVE.value:
            return np.zeros(self._time_interval_data.shape)

    @cycle.setter
    def cycle(self, value):
        self._cycle = value

    @property
    def dataset_values(self):
        if hasattr(self, "_dataset_values"):
            return self._dataset_values
        else:
            raise Exception("Dataset hasn't yet not been calculated !")

    @dataset_values.setter
    def dataset_values(self, value):
        self._dataset_values = value

    @property
    def time_interval_data(self):
        return self._time_interval_data
