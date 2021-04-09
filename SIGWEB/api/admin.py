from pyexpat import model

from django.apps import apps
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin

from .models import User



models = apps.get_models()

# admin.site.register(models)
# admin.site.unregister(User)
# admin.site.register(User, ModelAdmin)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'prenom', 'email', 'motdepass', 'compte_id', 'role']



