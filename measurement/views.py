# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer


# class SensorView(generics.ListCreateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer
#
#
# class SensorDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Sensor.objects.all().prefetch_related('measurements')
#     serializer_class = SensorDetailSerializer
#
#
# class MeasurementView(CreateAPIView):
#     queryset = Sensor.objects.all().prefetch_related('measurements')
#     serializer_class = MeasurementSerializer

class SensorView(APIView):

    def get(self, request):
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = SensorSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)


class SensorDetailView(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        sensor = Sensor.objects.get(id=pk)
        ser = SensorDetailSerializer(sensor)
        return Response(ser.data)

    def patch(self, request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            exampl = Sensor.objects.get(id=pk)
        except:
            return Response({'ошибка': "нет такого датчика"})
        ser = SensorSerializer(exampl, data=request.data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)


class MeasurementView(APIView):

    def post(self, request):
        ser = MeasurementSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)
