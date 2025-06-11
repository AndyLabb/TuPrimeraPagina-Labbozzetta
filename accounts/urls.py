from django.urls import path
from .views import signup_view
from aplicacion.views import register
from .views import enviar_mensaje
from accounts.views import eliminar_avatar


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('registro/', register, name='register'),
    path('enviar-mensaje/', enviar_mensaje, name='enviar_mensaje'),
    path('eliminar-avatar/', eliminar_avatar, name='eliminar_avatar'),

]
