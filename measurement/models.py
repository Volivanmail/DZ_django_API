from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)
    # date_create = models.DateField(auto_now_add=True)
    # date_update = models.DateField(auto_now=True)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True)  # на будущее
