from django.db import models
# from django.contrib.auth.models import AbstractUser

# Metodo 1: Elimina el modelo user que viene por defecto
#           y crea uno nuevo identico con las mismas
#           funcionalidades pero con los campos que quieras
#           agregar en la clase heredada de AbstractUser
#           Nota: este solo se realiza al principio del proyecto


# class User(AbstractUser):
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)


