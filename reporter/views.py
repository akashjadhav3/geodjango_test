from django.shortcuts import render
# from django.views.generic import TemplateView
# from django.core.serializers import serialize
# from django.http import HttpResponse
# from . models import Incidences

# class HomepageView(TemplateView):
#     template_name='reporter/index.html'

# def incidence_database(request):
#     cities_as_geojson=serialize('geojson', Incidences.objects.all())
#     return HttpResponse(cities_as_geojson, content_type='json')