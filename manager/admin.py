from django.contrib import admin
from .models import Device
from django.urls import path
from django import forms
from django.shortcuts import render, redirect
import csv
import io

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

class DeviceAdmin(admin.ModelAdmin):
    list_display = ["device_id","device_status","city","address"]

    change_list_template = "manager/device_change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
           
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            with io.TextIOWrapper(request.FILES["csv_file"], encoding="utf-8", newline='\n') as text_file:
                reader = csv.reader(text_file, delimiter=';')  
            # csv_file = request.FILES["csv_file"]
            # reader = csv.reader(csv_file, delimiter=';')
                for line in reader:
                    Device.objects.create(                        
                        device_id = line[0],                        
                        city = line[1],
                        zone = line[2],                        
                        address = line[3],
                        address_number = line[4],
                        zip_code = line[5],
                        complemento = line[6],
                        travel_time = line[7],
                        device_status = line[8], 
                        observacoes = line[9],
                    )

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )

admin.site.register(Device, DeviceAdmin)