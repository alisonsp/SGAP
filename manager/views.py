from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404
from .models import Device
from .forms import DeviceForm

def index(request):
  devices= Device.objects.all()
  template = loader.get_template('manager/list.html')
  context = {
        "devices": devices,
    }
  return HttpResponse(template.render(context, request))


def device_new(request):
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.device_id = request.user
            device.save()
            return redirect('device_detail', pk=device.pk)
    else:
        form = DeviceForm()
    return render(request, 'manager/device_edit.html', {'form': form})


def device_detail(request, pk):
    device = get_object_or_404(Device, device_id=pk)
    
    return render(request, "manager/device.html", {"device": device})