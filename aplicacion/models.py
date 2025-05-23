from django.db import models

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
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    edad = models.CharField(max_length=10)
    nivel = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Turno(models.Model):
    TIPOS_TURNO = [
        ('MD', 'Medio día'),
        ('DC', 'Día completo'),
    ]

    DIAS_SEMANA = [
        ('LU', 'Lunes'),
        ('MA', 'Martes'),
        ('MI', 'Miércoles'),
        ('JU', 'Jueves'),
        ('VI', 'Viernes'),
        ('SA', 'Sábado'),
        ('DO', 'Domingo'),
    ]

    tipo_turno = models.CharField(max_length=2, choices=TIPOS_TURNO)
    dias = models.CharField(max_length=100)
    alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE)
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_tipo_turno_display()} - {self.dias} - {self.alumno} - {self.instructor}"
