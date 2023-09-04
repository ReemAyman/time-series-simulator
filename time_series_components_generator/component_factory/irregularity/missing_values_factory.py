from time_series_components_generator.component_factory.irregularity.irregularity_component_factory import \
    IrregularityComponentFactory
from time_series_components_generator.irregularity_components.missing_values.missing_values_by_percentage import \
    MissingValuesByPercentage


class MissingValuesFactory(IrregularityComponentFactory):
    """
        A class for generating missing values different types.
    """

    def generate_components(self) -> dict:
        """
            Generate missing values instances for different types of time series data.
        Returns:
            dict: A dictionary contains different types of missing values.
        """
        missing_dict = {"percentage": MissingValuesByPercentage(self.series_data_component_values,
                                                                percentage_missing=self.component_parameters["percentage"])}
        return missing_dict
