from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Usuario(AbstractBaseUser, models.Model):
    nombre = models.CharField(max_length=255)
    rut = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=20, choices=(('admin', 'Administrador'), ('rrhh', 'Personal de RRHH')))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'rut', 'tipo_usuario']

    objects = BaseUserManager()

    def __str__(self):
        return f"{self.nombre} ({self.email})"

    def is_staff(self):
        return self.tipo_usuario == 'admin'

    def is_superuser(self):
        return self.tipo_usuario == 'admin'
    
class Permiso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    usuario = models.ManyToManyField(Usuario)

    def __str__(self):
        return f"{self.nombre} ({self.usuario.all()})"

from django.contrib.auth.models import User
# Create your models here.
class NewsCategory(models.Model):
    id_cat = models.AutoField(primary_key=True, db_column='idCategoria')
    category_title = models.CharField(max_length=50, blank=False, null=False)

class NewsPost(models.Model):
    post_title = models.CharField(max_length=200)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_story = models.CharField(max_length=2000)
    post_date = models.DateTimeField(auto_now_add=True)

class PostComment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(NewsPost, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    

