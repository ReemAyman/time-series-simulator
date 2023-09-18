# Generated by Django 4.1 on 2023-09-18 15:00

from django.db import migrations, models
import simulator_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator_api', '0003_alter_datasetconfiguration_simulation_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetconfiguration',
            name='producing_status',
            field=models.CharField(default='Submitted', max_length=5, validators=[simulator_api.models.validate_producing_status]),
        ),
        migrations.AlterField(
            model_name='simulationdata',
            name='meta_data',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='simulationdata',
            name='producer_type',
            field=models.CharField(default='csv', max_length=9, validators=[simulator_api.models.validate_producer_type]),
        ),
        migrations.AlterField(
            model_name='simulationdata',
            name='use_case_name',
            field=models.CharField(default='UC-<django.db.models.fields.CharField>', max_length=20),
        ),
    ]
