from django.urls import path

from .views import CreateSimulator, ListSimulator, UpdateSimulator

urlpatterns = [
    path('create', CreateSimulator.as_view(), name="CreateSimulator"),
    path('list', ListSimulator.as_view(), name="ListSimulator"),
    path('update', UpdateSimulator.as_view(), name="UpdateSimulator")
]
