from django import forms
from .models import Alumno, Turno, Instructor

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['nombre', 'apellido', 'nivel', 'antiguedad', 'especialidad']

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'email', 'edad', 'nivel']

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['tipo_turno', 'dias', 'alumno', 'instructor']

