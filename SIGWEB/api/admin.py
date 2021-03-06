from django.apps import apps
from django.contrib import admin
from .compte.models import Compte
from .donnees_raster.models import DonneesRaster
from .ligne.models import Ligne
from .models import User
from .models import Role
from .point.models import Point
from .polygone.models import Polygone

from django.contrib.gis import admin


admin.site.register(Compte)
admin.site.register(Role)
admin.site.register(DonneesRaster)
admin.site.register(Ligne)
admin.site.register(Polygone)
admin.site.register(Point)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'prenom', 'email', 'motdepass', 'compte_id', 'role']









