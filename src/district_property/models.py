from django.db import models

class DistrictProperty(models.Model):
    CD_MUN = models.CharField(
        max_length=255, 
        default=None, 
        null=True, 
        blank=True,
    )
    
    NM_MUN = models.CharField(
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
    
    AREA_KM2 = models.IntegerField(
        default=None, 
        null=True, 
        blank=True,
    )
    

    def __str__(self):
        return self.CD_MUN