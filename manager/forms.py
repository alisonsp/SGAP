from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    
    class Meta:
        model = Device
        fields = ('device_id','city','zone','address')
