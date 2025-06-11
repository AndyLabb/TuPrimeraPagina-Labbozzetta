from django.contrib import admin
from .models import Instructor, Alumno, Turno

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'especialidad', 'nivel', 'antiguedad')
    search_fields = ('nombre', 'apellido')
    list_filter = ('especialidad',)

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'edad', 'dni', 'nivel_ski', 'telefono_adulto')
    search_fields = ('nombre_completo', 'dni')

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('tipo_turno', 'fecha', 'alumno')
    list_filter = ('fecha', 'tipo_turno')
