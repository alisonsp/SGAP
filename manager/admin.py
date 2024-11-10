from django.contrib import admin
from .models import Device



class DeviceAdmin(admin.ModelAdmin):
    list_display = ["device_id","device_status","city","address"]

admin.site.register(Device, DeviceAdmin)