from django.db import models

# Create your models here.

class Device(models.Model):

    device_id = models.SmallIntegerField()
    city = models.CharField(max_length=20)
    zone = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    address_number = models.CharField(max_length=6)
    zip_code = models.CharField(max_length=8)
    travel_time = models.TimeField()
    complemento = models.CharField(max_length=250)
    device_status = models.BooleanField()
    observacoes = models.CharField(max_length=250)

    def __str__(self):
        return str(self.device_id)
