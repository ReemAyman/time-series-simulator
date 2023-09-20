from django.urls import path

from .views import CreateSimulator, ListSimulator, RunSimulator, StopSimulator

urlpatterns = [
    path('create', CreateSimulator.as_view(), name="CreateSimulator"),
    path('list', ListSimulator.as_view(), name="ListSimulator"),
    path('stop', StopSimulator.as_view(), name="StopSimulator"),
    path('run', RunSimulator.as_view(), name="RunSimulator")
]
