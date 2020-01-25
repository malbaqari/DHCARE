from django.contrib import admin

from .models import provider, department, appointment

admin.site.register(provider)
admin.site.register(department)
admin.site.register(appointment)
