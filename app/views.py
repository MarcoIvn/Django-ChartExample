from django.shortcuts import render
from .models import Alumno
from django.db.models import Count
import json
from django.db.models import Avg

def reporte_alumnos(request):
    # Obtiene todos los registros de la tabla Alumno
    alumnos = Alumno.objects.all()

    # Obtener datos para la gráfica
    datos = Alumno.objects.values_list('id_alumno', 'calificacion').order_by('id_alumno')
    datos_grafica = [{'id_alumno': id_alumno, 'calificacion': float(calificacion)} for id_alumno, calificacion in datos]
    promedio_calificaciones = alumnos.aggregate(Avg('calificacion'))['calificacion__avg']
    print(datos_grafica)
    # Convierte los datos a formato JSON
    datos_grafica_json = json.dumps(datos_grafica)

    cxt = {
        'alumnos': alumnos,
        'promedio_calificaciones': promedio_calificaciones,
        'datos_grafica_json': datos_grafica_json,
    }
    return render(request, 'app/reporte_alumnos.html', cxt)

def index(request):
    return render(request, 'app/index.html')