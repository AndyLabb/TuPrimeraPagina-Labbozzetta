from django.urls import path
from . import views

urlpatterns = [
    path('crear_alumno/', views.crear_alumno, name='crear_alumno'),
    path('crear_turno/', views.crear_turno, name='crear_turno'),
    path('crear_instructor/', views.crear_instructor, name='crear_instructor'),
    path('buscar_turnos/', views.buscar_turnos, name='buscar_turnos'),

]
