from django.db import models
from django.db.models.functions import Lower
from django.db.models import F

# Create your models here.
class Stations(models.Model):
    station = models.CharField(max_length=200)
    line = models.CharField(max_length=200)
    admarea = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True, auto_created=True)

    def __str__(self):
        return self.station

    class Meta:
        ordering = ('station',)
