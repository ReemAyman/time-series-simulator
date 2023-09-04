from time_series_components_generator.component_factory.irregularity.irregularity_component_factory import \
    IrregularityComponentFactory
from time_series_components_generator.irregularity_components.outliers.outliers_by_percentage import \
    OutliersByPercentage


class OutliersFactory(IrregularityComponentFactory):
    """
        A class for generating outliers different types.
    """

    def generate_components(self) -> dict:
        """
            Generate outliers instances for different types of time series data.
        Returns:
            dict: A dictionary contains different types of outliers.
        """
        outliers_dict = {"percentage": OutliersByPercentage(self.series_data_component_values,
                                                            percentage_outliers=self.component_parameters[
                                                                "percentage"])}
        return outliers_dict
