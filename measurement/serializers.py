from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from measurement.models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['id', 'temperature', 'created_at']


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True)

    class Meta:
        model = Sensor
        # fields = "__all__"
        fields = ['id', 'name', 'description', 'date_create', 'date_update', 'measurements']

