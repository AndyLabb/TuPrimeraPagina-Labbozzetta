from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from accounts.views import signup_view
from accounts.views import eliminar_avatar
from .views import (
    home,CrearAlumnoView, CrearTurnoView, CrearInstructorView, BuscarTurnoView, editar_perfil, SobreMiView
)



urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('crear-alumno/', CrearAlumnoView.as_view(), name='crear_alumno'),
    path('crear-turno/', CrearTurnoView.as_view(), name='crear_turno'),
    path('crear-instructor/', CrearInstructorView.as_view(), name='crear_instructor'),
    path('buscar-turnos/', BuscarTurnoView.as_view(), name='buscar_turnos'),
    path('editar-perfil/', editar_perfil, name='editar_perfil'),
    path('signup/', signup_view, name='signup'),
    path('sobre-mi/', SobreMiView.as_view(), name='sobre_mi'),
    
]
