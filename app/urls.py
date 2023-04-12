from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reporte_alumnos/', views.reporte_alumnos, name='reporte_alumnos'),
]