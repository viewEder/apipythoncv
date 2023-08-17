from django.db import models
# importamos la clase abstracta de usuarios:
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from ckeditor.fields import RichTextField

# Create your models here.

class UserManager(BaseUserManager):
    """Define a model manager for User model"""
    def create_user(self, email, password, **extra_fields):
        # Validamos la existencia de email:
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using = self._db)

        return user

    # Method for superUser:
    def create_super_user(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)

        return user


class User(AbstractUser, PermissionsMixin):
    TYPE_ID = [
        ("Registro Civil", "Registro Civil"),
        ("Tarjeta de Identidad", "Tarjeta de Identidad"),
        ("Cédula de Ciudadanía", "Cédula de Ciudadanía"),
        ("Cédula de Extranjería", "Cédula de Extranjería"),
        ("Pasaporte", "Pasaporte"),
        ("Permiso Temporal", "Permiso Temporal"),
    ]

    email = models.EmailField('Correo Electrónico', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    type_id = models.CharField(verbose_name='Tipo de Identificación', max_length=50, choices=TYPE_ID)
    identification = models.CharField(verbose_name='Número de Identificación', max_length=50)
    photo = models.ImageField(verbose_name='Foto de Perfil', upload_to='img/usuarios/')
    country = models.CharField(verbose_name='Pais de Residencia', max_length=255)
    city = models.CharField(verbose_name='Ciudad de Residencia', max_length=255)
    address = models.TextField(verbose_name='Direccion de Residencia')
    phone = models.CharField(verbose_name='Teléfono', max_length=20, null=True, blank=True)
    birthday = models.DateField(verbose_name="Fecha de Nacimiento", null=True, blank=True)
    occupation_job = models.CharField(verbose_name='Ocupacion', max_length=150)
    relocate =  models.BooleanField('Disponible para desplazarse', default=False)
    is_recruiter = models.BooleanField('Recutador', default=False)
    created =models.DateTimeField(auto_now_add=True)
    modified =models.DateTimeField(auto_now=True)

    objects = UserManager()


class Links(models.Model):
    TYPE_LINK = [
        ("Repositorio", "Repositorio"),
        ("LinkedIN", "LinkedIN"),
        ("WebSite", "WebSite"),
        ("Red Social", "Red Social"),
    ]

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    type_link = models.CharField(verbose_name='Tipo de Enlace', max_length=50, choices=TYPE_LINK)
    link_url = models.URLField(verbose_name='Link')
    created =models.DateTimeField(auto_now_add=True)
    modified =models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name ="Enlace"
        verbose_name_plural ="Enlaces"

    def __str__(self):
        return f'{self.link_url}'

class ResumeUser(models.Model):
    RESUME_SECCTION = [
        ("PP", "Perfil Profesional"),
        ("RR", "Resumen Profesional"),
        ("RF", "Resume Hechos"),
        ("RS", "Resumen Sumario"),
        ("RA", "Resumen Adjetivos"),
        ("RC", "Resumen Contacto"),
    ]

    type_resume = models.CharField(verbose_name='Tipo de Resumen', max_length=20, choices=RESUME_SECCTION)
    resumes = RichTextField(verbose_name='Resumen')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name ="Resumen"
        verbose_name_plural ="Resumenes"

    def __str__(self):
        for resumen in self.RESUME_SECCTION:
            if (resumen[0] == self.type_resume):
                return f'{resumen[0]}'