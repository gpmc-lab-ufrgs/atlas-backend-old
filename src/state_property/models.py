from django.db import models

class StateProperty(models.Model):
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
        return self.CD_UF