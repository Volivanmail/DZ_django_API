# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response

from measurement.models import Sensor
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all().prefetch_related('measurements')
    serializer_class = SensorSerializer


class SensorDetailView(ListCreateAPIView):
    queryset = Sensor.objects.all().prefetch_related('measurements')
    serializer_class = SensorDetailSerializer


class MeasurementView(ListAPIView):
    queryset = Sensor.objects.all().prefetch_related('measurements')
    serializer_class = MeasurementSerializer
