# Generated by Django 4.1 on 2023-09-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator_api', '0006_alter_datasetconfiguration_producing_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulationdata',
            name='use_case_name',
            field=models.CharField(default='UC-1', max_length=50),
        ),
    ]