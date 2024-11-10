from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.index, name='list'),
    path('device/<int:pk>/', views.device_detail, name='device_detail'),
    path('device/new/', views.device_new, name='device_new'),
]