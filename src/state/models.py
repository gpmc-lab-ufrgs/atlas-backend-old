from django.contrib.gis.db import models

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
    
    CD_UF = models.CharField(
        max_length=255, 
        default=None, 
        null=True, 
        blank=True,
    )
    
    POPULATION = models.IntegerField(
        default=None, 
        null=True, 
        blank=True,
    )
    
    NM_UF = models.CharField(
        max_length=255, 
        default=None, 
        null=True, 
        blank=True,
    )
    
    SIGLA_UF = models.CharField(
        max_length=255, 
        default=None, 
        null=True, 
        blank=True,
    )
    
    NM_REGIAO = models.CharField(
        max_length=255, 
        default=None, 
        null=True, 
        blank=True,
    )
    
    def __str__(self):
        return self.name