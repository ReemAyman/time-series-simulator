from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_producing_status(producing_status):
    """
        Validate producing status input [Submitted, Running, Succeeded, Failed] created in a dataset.
    Args:
        producing_status: the producing status input.

    Returns:
        Raising an exception if it is not valid.
    """
    if producing_status != "Submitted" and producing_status != "Running" \
            and producing_status != "Succeeded" and producing_status != "Failed":
        raise ValidationError(
            _(f"{producing_status} is not a valid status."),
            params={"value": producing_status},
        )


def validate_noise_level(noise_level):
    """
        Validate noise level input [Low, Medium, High] created in a dataset.
    Args:
        noise_level: the noise level input.

    Returns:
        Raising an exception if it is not valid.
    """
    if noise_level != "Low" and noise_level != "Medium" and noise_level != "High":
        raise ValidationError(
            _(f"{noise_level} is not a valid noise level."),
            params={"value": noise_level},
        )


def validate_seasonality_type(seasonality_type):
    """
        Validate seasonality type input [Daily, Weekly, Monthly] created in a seasonality instance.
    Args:
        seasonality_type: the seasonality type input.

    Returns:
        Raising an exception if it is not valid.
    """
    if seasonality_type != "Daily" and seasonality_type != "Weekly" and seasonality_type != "Monthly":
        raise ValidationError(
            _(f"{seasonality_type} is not a valid seasonality type."),
            params={"value": seasonality_type},
        )


def validate_producer_type(producer_type):
    """
        Validate producer type [csv, kafka] of dataset.
    Args:
        producer_type: the producer type input.

    Returns:
        Raising an exception if it is not valid.
    """
    if producer_type != "csv" and producer_type != "Kafka":
        raise ValidationError(
            _(f"{producer_type} is not a valid producer type."),
            params={"value": producer_type},
        )


def validate_time_series_type(time_series_type):
    """
        Validate time series input [additive, multiplicative] created in a simulation instance.
    Args:
        time_series_type: the producing status input.

    Returns:
        Raising an exception if it is not valid.
    """
    if time_series_type != "additive" and time_series_type != "multiplicative":
        raise ValidationError(
            _(f"{time_series_type} is not a valid time series type."),
            params={"value": time_series_type},
        )


class SimulationData(models.Model):
    """
    A model for simulation data.
    """
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    type = models.CharField(max_length=14, validators=[validate_time_series_type], default="additive")
    use_case_name = models.CharField(max_length=50, unique=True)
    meta_data = models.CharField(max_length=200, default="")
    producer_type = models.CharField(max_length=9, validators=[validate_producer_type], default="csv")
    process_id = models.IntegerField(default=-1)


class DatasetConfiguration(models.Model):
    """
    A model for setting configurations for a single dataset.
    """
    simulation_data = models.ForeignKey(SimulationData,  related_name='datasets', on_delete=models.CASCADE)
    frequency = models.CharField(max_length=5)
    trend_coefficients = ArrayField(models.IntegerField(), default=[0])
    missing_percentage = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)])
    outlier_percentage = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)])
    noise_level = models.IntegerField()
    cycle_amplitude = models.IntegerField()
    cycle_frequency = models.IntegerField()
    producing_status = models.CharField(max_length=14, validators=[validate_producing_status], default="Submitted")


class SeasonalityModel(models.Model):
    """
    A model for setting a seasonality for a dataset.
    """
    dataset_config = models.ForeignKey(DatasetConfiguration, related_name='seasonality_components', on_delete=models.CASCADE)
    frequency = models.CharField(max_length=7, validators=[validate_seasonality_type])
    multiplier = models.IntegerField()
    phase_shift = models.IntegerField()
    amplitude = models.IntegerField()
