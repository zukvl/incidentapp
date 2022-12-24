from django.contrib import admin
from incidentapp.models import component, incident

# Register your models here.
admin.site.register(component)
admin.site.register(incident)