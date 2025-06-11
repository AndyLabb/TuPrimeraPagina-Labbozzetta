from django.shortcuts import render, redirect
from .forms import AlumnoForm, TurnoForm, InstructorForm
from .models import Turno, Alumno, Instructor
from django.db.models import Q,Case, When, CharField, Value
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, UpdateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from aplicacion.forms import UserUpdateForm
from accounts.forms import UserProfileForm,CustomUserCreationForm
from accounts.models import UserProfile
from django.contrib.auth import login
from django.shortcuts import redirect


# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def editar_perfil(request):
    user = request.user
    perfil, creado = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=perfil)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = UserProfileForm(instance=perfil)

    return render(request, 'editar_perfil.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'perfil': perfil
    })

@login_required
def eliminar_avatar(request):
    perfil = request.user.profile
    if perfil.avatar:
        perfil.avatar.delete()
    return redirect('editar_perfil')

class CrearAlumnoView(LoginRequiredMixin, CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'crear_alumno.html'
    success_url = reverse_lazy('crear_turno')

    def form_valid(self, form):
        form.instance.usuario = self.request.user  
        return super().form_valid(form)

class CrearTurnoView(LoginRequiredMixin, CreateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'crear_turno.html'
    success_url = reverse_lazy('crear_turno')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # pasa el user al form
        return kwargs

class CrearInstructorView(LoginRequiredMixin, CreateView):
    model = Instructor
    form_class = InstructorForm
    template_name = 'crear_instructor.html'
    success_url = reverse_lazy('crear_instructor')

class BuscarTurnoView(LoginRequiredMixin, ListView):
    model = Turno
    template_name = 'buscar_turnos.html'
    context_object_name = 'resultados'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        user = self.request.user

        if not query:
            return Turno.objects.none()

        turnos = Turno.objects.annotate(
            tipo_turno_legible=Case(
                When(tipo_turno='MD', then=Value('Medio día')),
                When(tipo_turno='DC', then=Value('Día completo')),
                output_field=CharField()
            )
        )

        return turnos.filter(
            Q(alumno__usuario=user),  
            Q(alumno__nombre_completo__icontains=query) |
            Q(fecha__icontains=query) |
            Q(tipo_turno__icontains=query) |
            Q(tipo_turno_legible__icontains=query)
    )


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)  
            login(request, user)  
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class SobreMiView(TemplateView):
    template_name = "sobre_mi.html"
