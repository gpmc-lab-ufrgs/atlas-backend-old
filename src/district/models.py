from django.contrib.gis.db import models

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
    
    MUNICIPALITY_CODE = models.CharField(
        max_length=255, 
        default=None, 
        null=True, 
        blank=True,
    )
    
    MUNICIPALITY_NAME = models.CharField(
        max_length=255, 
        default=None, 
        null=True, 
        blank=True,
    )
    
    ACRONYM_FU = models.CharField(
        max_length=255, 
        default=None, 
        null=True, 
        blank=True,
    )
    
    AREA_KM2 = models.IntegerField(
        default=None, 
        null=True, 
        blank=True,
    )
    
    def __str__(self):
        return self.name