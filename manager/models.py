from django.db import models
# Create your models here.

class Device(models.Model):

    device_id = models.SmallIntegerField(verbose_name="ID")
    device_status = models.BooleanField(verbose_name="Status")
    city = models.CharField(max_length=20, verbose_name="Cidade")
    zone = models.CharField(max_length=20, verbose_name="Região")
    address = models.CharField(max_length=20, verbose_name="Endereço")
    address_number = models.CharField(max_length=6, verbose_name="Número")
    complemento = models.CharField(max_length=250, verbose_name="Complemento")
    zip_code = models.CharField(max_length=9, verbose_name="CEP")
    travel_time = models.TimeField( verbose_name="Tempo de deslocamento")
    observacoes = models.CharField(max_length=250, verbose_name="Obs")
