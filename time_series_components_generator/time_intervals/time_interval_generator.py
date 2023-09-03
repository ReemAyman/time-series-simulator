import datetime
import pandas as pd


class TimeIntervalGenerator:
    """
    An abstract class for generating time series interval.
    """

    def __init__(self, start_date: datetime, end_date: datetime, frequency: str):
        """
        Initializing time series interval instance by start time and frequency.

        Args:
            start_date: the start date of the time interval.
            end_date: the end date of the time interval.
            frequency: the sampling frequency of the time points in the time interval.
        """
        self.start_date = start_date
        self.end_date = end_date
        self.frequency = frequency

    def generate_time_interval(self) -> pd.DatetimeIndex:
        """
        Generate time interval of the time series data.

        Returns:
            pandas.DatetimeIndex: The generated time index.
        """
        date_interval = pd.date_range(start=self.start_date, end=self.end_date, freq=self.frequency)
        return date_interval
