
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import MensajeForm
from .models import UserProfile

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.usuario = request.user
            mensaje.save()
            return redirect('home')
    else:
        form = MensajeForm()
    return render(request, 'enviar_mensaje.html', {'form': form})

@login_required
def eliminar_avatar(request):
    perfil = request.user.profile
    if perfil.avatar:
        perfil.avatar.delete()
        perfil.save()
    return redirect('editar_perfil')