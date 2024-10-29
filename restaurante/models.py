from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, nombre, contraseña=None):
        if not correo:
            raise ValueError('El usuario debe tener un correo electrónico')
        usuario = self.model(
            correo=self.normalize_email(correo),
            nombre=nombre,
        )
        usuario.set_password(contraseña)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo, nombre, contraseña=None):
        usuario = self.create_user(
            correo,
            contraseña=contraseña,
            nombre=nombre,
        )
        usuario.is_admin = True
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100, unique=True)
    contraseña = models.CharField(max_length=255)

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre']

    objects = UsuarioManager()

    def __str__(self):
        return self.correo

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Rol(models.Model):
    nombre = models.CharField(max_length=50)

class Permiso(models.Model):
    nombre = models.CharField(max_length=50)



class UsuarioRol(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

class RolPermiso(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    administrador = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL)

class AdministradorRestaurante(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

class Mesa(models.Model):
    numero = models.IntegerField()
    capacidad = models.IntegerField()
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

class Horario(models.Model):
    dia_semana = models.CharField(max_length=20)
    hora_apertura = models.TimeField()
    hora_cierre = models.TimeField()
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

class Reserva(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=50, default='Pendiente')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
