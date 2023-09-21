import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from time_series_components_generator.trasformers.transformer import Transformer


class MinMaxScalerTransformer(Transformer):
    """
        A class for applying normalization on the time series data.
    """
    def __init__(self):
        """
            Initializing the normalizer transformer.
        """
        self.scaler = MinMaxScaler(feature_range=(-1, 1))

    def transform(self, data_component_values):
        return self.scaler.fit_transform(data_component_values.values.reshape(-1, 1)).reshape(data_component_values.shape)
