# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from measurement.models import Sensor
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer


class SensorView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all().prefetch_related('measurements')
    serializer_class = SensorDetailSerializer


class MeasurementView(ListAPIView):
    queryset = Sensor.objects.all().prefetch_related('measurements')
    serializer_class = MeasurementSerializer
