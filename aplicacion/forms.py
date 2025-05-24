from django import forms
from .models import Alumno, Turno, Instructor

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control form-control-dark', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control form-control-dark', 'placeholder': 'Apellido'}),
            'nivel': forms.TextInput(attrs={
                'class': 'form-control form-control-dark', 'placeholder': 'Nivel'}),
            'antiguedad': forms.TextInput(attrs={
                'class': 'form-control form-control-dark', 'placeholder': 'Antigüedad'}),
            'especialidad': forms.Select(attrs={
                'class': 'form-select form-control-dark'}),
        }

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-dark'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control form-control-dark'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-dark'}),
            'edad': forms.TextInput(attrs={'class': 'form-control form-control-dark'}),
            'nivel': forms.TextInput(attrs={'class': 'form-control form-control-dark'}),
        }

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['tipo_turno', 'fecha', 'alumno', 'instructor']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
