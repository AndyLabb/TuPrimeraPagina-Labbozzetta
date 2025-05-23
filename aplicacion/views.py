from django.shortcuts import render, redirect
from .forms import AlumnoForm, TurnoForm, InstructorForm
from .models import Turno
from django.db.models import Q

# Create your views here.

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_turno')  
    else:
        form = AlumnoForm()
    return render(request, 'crear_alumno.html', {'form': form})

def crear_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_turno')
    else:
        form = TurnoForm()
    return render(request, 'crear_turno.html', {'form': form})

def crear_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_instructor')
    else:
        form = InstructorForm()
    return render(request, 'crear_instructor.html', {'form': form})

def buscar_turnos(request):
    resultados = []
    query = ""

    if request.method == "GET":
        query = request.GET.get("q", "")
        if query:
            resultados = Turno.objects.filter(
                Q(alumno__nombre__icontains=query) | Q(alumno__apellido__icontains=query)
            )

    return render(request, "buscar_turnos.html", {"resultados": resultados, "query": query})
