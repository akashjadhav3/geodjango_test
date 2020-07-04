from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
from djgeojson.fields import PolygonField

class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    objects = GeoManager()
    geom = PolygonField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'incidences'
    
