from django.contrib import admin
from .models import Incidences

class IncidencesAdmin(admin.ModelAdmin):
    list_display = ('name', 'location') # user for show column name

admin.site.register(Incidences, IncidencesAdmin)