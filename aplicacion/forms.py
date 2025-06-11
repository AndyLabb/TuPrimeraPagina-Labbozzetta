from django import forms
from .models import Alumno, Turno, Instructor
from django.contrib.auth.models import User
from django.forms.widgets import DateInput

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

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
        exclude = ['usuario'] 
        fields = '__all__'
        widgets = {
            'usa_lentes': forms.RadioSelect(choices=[(True, 'Sí'), (False, 'No')]),
            'alergias': forms.Textarea(attrs={'rows': 2}),
            'intervenciones_medicas': forms.Textarea(attrs={'rows': 2}),
            'motricidad_reducida': forms.Textarea(attrs={'rows': 2}),
            'info_extra': forms.Textarea(attrs={'rows': 2}),
            'historial_clases': forms.Textarea(attrs={'rows': 2}),
        }


class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['tipo_turno', 'fecha', 'alumno']
        widgets = {
            'fecha': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['alumno'].queryset = Alumno.objects.filter(usuario=user)