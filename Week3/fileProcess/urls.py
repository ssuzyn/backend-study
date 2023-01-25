from django.urls import path, include
from fileProcess import views

urlpatterns = [
    path('', views.main)
]