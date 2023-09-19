from django.contrib.gis.db import models

class District(models.Model):
    name = models.CharField(max_length=255, default="district")
    type = models.CharField(max_length=255, default="Feature")
    geometry = models.MultiPolygonField(default=None,blank=True)
    POPULATION = models.IntegerField(default=None, null=True, blank=True)
    CD_MUN = models.CharField(max_length=255, default=None, null=True, blank=True)
    NM_MUN = models.CharField(max_length=255, default=None, null=True, blank=True)
    SIGLA_UF = models.CharField(max_length=255, default=None, null=True, blank=True)
    AREA_KM2 = models.IntegerField(default=None, null=True, blank=True)
    
    def __str__(self):
        return self.name

    @property
    def properties(self):
        return {
            "CD_MUN": self.CD_MUN,
            "POPULATION": self.POPULATION,
            "NM_MUN": self.NM_MUN,
            "SIGLA_UF": self.SIGLA_UF,
            "AREA_KM2": self.AREA_KM2,
        }

