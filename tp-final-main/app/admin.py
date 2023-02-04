from django.contrib import admin

from .models import Client, Entreprise, Reclamation

# Register your models here.

admin.site.register(Entreprise)
admin.site.register(Client)
admin.site.register(Reclamation)