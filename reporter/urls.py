from django.urls import path
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
# from . views import *
from .models import Incidences

urlpatterns = [
    # path('',HomepageView.as_view(), name='home'),
    path('',TemplateView.as_view(template_name='reporter/index.html'), name='home'),
    # path('inciedence_data/',incidence_database, name='city'), 
    path('data.geojson/',GeoJSONLayerView.as_view(model=Incidences), name='data'),
]