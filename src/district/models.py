from django.contrib.gis.db import models

from district_property.models import DistrictProperty

class District(models.Model):
    name = models.CharField(
        max_length=255, 
        default="district",
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
        DistrictProperty, 
        on_delete=models.CASCADE, 
        default=None
    )
    
    def __str__(self):
        return self.name