from django.contrib.gis.db import models

class State(models.Model):
    name = models.CharField( max_length=255, default="state")
    type = models.CharField(max_length=255, default="Feature")
    geometry = models.MultiPolygonField(default=None,blank=True)
    CD_UF = models.CharField(max_length=255, default=None, null=True, blank=True)
    POPULATION = models.IntegerField(default=None, null=True, blank=True)
    NM_UF = models.CharField(max_length=255, default=None, null=True, blank=True)
    SIGLA_UF = models.CharField(max_length=255, default=None, null=True, blank=True,)
    NM_REGIAO = models.CharField(max_length=255, default=None, null=True, blank=True)
    
    def __str__(self):
        return self.name

    @property
    def properties(self):
        return {
            "CD_UF": self.CD_UF,
            "POPULATION": self.POPULATION,
            "NM_UF": self.NM_UF,
            "SIGLA_UF": self.SIGLA_UF,
            "NM_REGIAO": self.NM_REGIAO,
        }
