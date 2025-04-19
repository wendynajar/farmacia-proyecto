from django.contrib import admin
from .models import Productos, Descuentos, VistaDescuentos

# Register your models here.
admin.site.register(Productos)
admin.site.register(Descuentos)
admin.site.register(VistaDescuentos)