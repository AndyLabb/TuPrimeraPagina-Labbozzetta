from django.contrib import admin
from .models import Instructor, Alumno, Turno

# Register your models here.
admin.site.register(Instructor)
admin.site.register(Alumno)
admin.site.register(Turno)