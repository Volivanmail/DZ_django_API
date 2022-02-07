from django.urls import path

from measurement.views import MeasurementView, SensorDetailView, SensorView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
    path('measurements/<pk>/', MeasurementView.as_view()),
]
