from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator

# Create your models here.
    
class Instructor(models.Model):
    ESPECIALIDADES = [
        ('ski', 'Ski'),
        ('snowboard', 'Snowboard'),
    ]

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nivel = models.CharField(max_length=10)
    antiguedad = models.CharField(max_length=15)
    especialidad = models.CharField(max_length=10, choices=ESPECIALIDADES)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.get_especialidad_display()})"


class Alumno(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alumnos")  
    nombre_completo = models.CharField(max_length=100)
    edad = models.IntegerField(validators=[MinValueValidator(1)])
    dni = models.CharField(max_length=20)
    nacionalidad = models.CharField(max_length=50)
    telefono_adulto = models.CharField(max_length=50)
    seguro_vida = models.CharField(max_length=50)
    obra_social = models.CharField(max_length=50)
    alergias = models.TextField(blank=True)
    intervenciones_medicas = models.TextField(blank=True)
    motricidad_reducida = models.TextField(blank=True)
    usa_lentes = models.BooleanField(default=False)
    info_extra = models.TextField(blank=True)
    nivel_ski = models.CharField(max_length=50)
    historial_clases = models.TextField(blank=True)

    def __str__(self):
        return self.nombre_completo

    def mostrar_info(self):
        return f"{self.nombre_completo} - {self.edad} años"


class Turno(models.Model):
    TIPOS_TURNO = [
        ('MD', 'Medio día'),
        ('DC', 'Día completo'),
    ]

    tipo_turno = models.CharField(max_length=2, choices=TIPOS_TURNO)
    fecha = models.DateField(null=True, blank=True)  # <--- a futuro modificare esta linea para hacerla mas dinamica y poder elegir varios dias

    alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.get_tipo_turno_display()} - {self.fecha} - {self.alumno} "
    
