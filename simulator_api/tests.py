from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from simulator_api.models import SimulationData, DatasetConfiguration
from django.db import connection

from simulator_api.utils import simulator_thread


class TestSimulator(APITestCase):
    fixtures = ['simulation_data.json']

    def setUp(self) -> None:

        self.process_id = simulator_thread.ident

    def test_create_simulator_success(self):
        """
        Ensure create a new simulator object.
        """
        data = {
            "use_case_name": "simulator31",
            "start_date": "2021-01-01",
            "end_date": "2022-01-01",
            "type": "MULTIPLICATIVE",
            "datasets": [
                {
                    "frequency": "10H",
                    "trend_coefficients": [0, 2, 1, 3],
                    "missing_percentage": 0.06,
                    "outlier_percentage": 0.1,
                    "noise_level": 10,
                    "cycle_amplitude": 3,
                    "cycle_frequency": 1,
                    "seasonality_components": [
                        {
                            "frequency": "Weekly",
                            "multiplier": 1,
                            "phase_shift": 0,
                            "amplitude": 3
                        },
                        {
                            "frequency": "Daily",
                            "multiplier": 2,
                            "phase_shift": 9,
                            "amplitude": 5
                        }
                    ]
                },
                {
                    "frequency": "2H",
                    "trend_coefficients": [0, 2, 1, 3],
                    "missing_percentage": 0.06,
                    "outlier_percentage": 0.1,
                    "noise_level": 10,
                    "cycle_amplitude": 3,
                    "cycle_frequency": 1,
                    "seasonality_components": [
                        {
                            "frequency": "Weekly",
                            "multiplier": 1,
                            "phase_shift": 0,
                            "amplitude": 3
                        },
                        {
                            "frequency": "Monthly",
                            "multiplier": 2,
                            "phase_shift": 9,
                            "amplitude": 5
                        }
                    ]
                }
            ]
        }
        self.response = self.client.post(reverse('CreateSimulator'), data=data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(SimulationData.objects.count(), 2)
        sim_data = SimulationData.objects.get(use_case_name='simulator31')
        self.assertEqual(sim_data.use_case_name, 'simulator31')
        self.assertIsNotNone(sim_data.datasets)

    def test_list_simulator_success(self):
        """
        Ensure list all simulators.
        """
        self.response = self.client.get(reverse('ListSimulator'))
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(self.response.data['results']), 1)
        self.assertEqual(len(self.response.data['results'][0]['datasets']), 1)

    def test_run_simulator_success(self):
        """
        Ensure run a simulator object.
        """
        data = {
            'process_id': -1
        }
        self.response = self.client.patch(reverse('RunSimulator'), data=data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        dsets = DatasetConfiguration.objects.filter(simulation_data_id=1)
        for d in dsets:
            self.assertEqual(d.producing_status, 'Running')

    def test_stop_simulator_success(self):
        """
        Ensure stop a simulator object.
        """
        data = {
            'process_id': -1
        }
        self.response = self.client.patch(reverse('StopSimulator'), data=data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        dsets = DatasetConfiguration.objects.filter(simulation_data_id=1)
        for d in dsets:
            self.assertEqual(d.producing_status, 'Failed')
        connection.close()
