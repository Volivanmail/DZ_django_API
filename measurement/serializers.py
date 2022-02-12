from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from measurement.models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    # created_at = serializers.DateField(read_only=True)
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True,many=True)

    class Meta:
        model = Sensor
        # fields = "__all__"
        fields = ['id', 'name', 'description', 'measurements']

