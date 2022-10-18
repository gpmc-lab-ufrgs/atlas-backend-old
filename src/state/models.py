from django.contrib.gis.db import models

from state_property.models import StateProperty

class State(models.Model):
    name = models.CharField(
        max_length=255, 
        default="state",
        primary_key=True
    )
    
    type = models.CharField(
        max_length=255, 
        default="Feature"
    )
    
    geometry = models.MultiPolygonField(
        default=None,
        blank=True
    )
    
    properties = models.ForeignKey(
        StateProperty, 
        on_delete=models.CASCADE, 
        default=None
    )
    
    def __str__(self):
        return self.name