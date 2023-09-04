from time_series_components_generator.component_factory.irregularity.irregularity_component_factory import \
    IrregularityComponentFactory
from time_series_components_generator.irregularity_components.noise.linear_noise import LinearNoise


class NoiseFactory(IrregularityComponentFactory):
    """
        A class for generating noise different types.
    """
    def generate_components(self) -> dict:
        """
            Generate noise instances for different types of time series data.
        Returns:
            dict: A dictionary contains different types of noise.
        """
        noise_dict = {"percentage": LinearNoise(self.series_data_component_values, self.component_parameters["percentage"])}
        return noise_dict
