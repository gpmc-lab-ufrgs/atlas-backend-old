from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Sectors(models.Model):
    cd_setor = models.CharField(max_length=255)
    cd_sit = models.CharField(max_length=255,default=None,null=True,blank=True)
    nm_sit = models.CharField(max_length=255,default=None,null=True,blank=True)
    cd_uf = models.CharField(max_length=255,default=None,null=True,blank=True)
    nm_uf = models.CharField(max_length=255,default=None,null=True,blank=True)
    sigla_uf = models.CharField(max_length=255,default=None,null=True,blank=True)
    cd_mun = models.CharField(max_length=255,default=None,null=True,blank=True)
    nm_mun = models.CharField(max_length=255,default=None,null=True,blank=True)
    cd_dist = models.CharField(max_length=255,default=None,null=True,blank=True)
    nm_dist = models.CharField(max_length=255,default=None,null=True,blank=True)
    cd_subdist = models.CharField(max_length=255,default=None,null=True,blank=True)
    nm_subdist = models.CharField(max_length=255,default=None,null=True,blank=True)
    geom = models.MultiPolygonField(default=None,blank=True)

    def __str__(self):
        return self.cd_setor

class SectorsSensus(models.Model):
    cd_setor = models.CharField(max_length=255)
    cd_sit = models.CharField(max_length=255,default=None,null=True,blank=True)
    nm_sit = models.CharField(max_length=255,default=None,null=True,blank=True)
    cd_uf = models.CharField(max_length=255,default=None,null=True,blank=True)
    nm_uf = models.CharField(max_length=255,default=None,null=True,blank=True)
    sigla_uf = models.CharField(max_length=255,default=None,null=True,blank=True)
    cd_mun = models.CharField(max_length=255,default=None,null=True,blank=True)
    nm_mun = models.CharField(max_length=255,default=None,null=True,blank=True)
    cd_dist = models.CharField(max_length=255,default=None,null=True,blank=True)
    nm_dist = models.CharField(max_length=255,default=None,null=True,blank=True)
    cd_subdist = models.CharField(max_length=255,default=None,null=True,blank=True)
    nm_subdist = models.CharField(max_length=255,default=None,null=True,blank=True)
    geom = models.MultiPolygonField(default=None,blank=True)

    def __str__(self):
        return self.cd_setor
