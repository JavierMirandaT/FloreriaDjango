from django.contrib import admin
from .models import Tipo, Flora

# Register your models here.

class FloraAdmin(admin.ModelAdmin):
    list_display = ["nombre", "valor", "tipo", "disponibilidad"]
    list_editable = ["valor", "disponibilidad"]

admin.site.register(Tipo)
admin.site.register(Flora,FloraAdmin)