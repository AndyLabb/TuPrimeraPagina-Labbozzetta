from django.contrib.auth.models import User
from django.db import models
import os

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

    def save(self, *args, **kwargs):
        try:
            this = UserProfile.objects.get(id=self.id)
            if this.avatar != self.avatar and this.avatar:
                if os.path.isfile(this.avatar.path):
                    os.remove(this.avatar.path)
        except UserProfile.DoesNotExist:
            pass
        super().save(*args, **kwargs)


class Mensaje(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    asunto = models.CharField(max_length=200)
    contenido = models.TextField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.asunto}"