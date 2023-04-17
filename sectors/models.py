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
    ID = models.BigIntegerField(max_length=255, default=None, null=True, blank=True)
    cd_geocodi = models.CharField(max_length=255,primary_key=True)
    tipo = models.CharField(max_length=255, default=None, null=True, blank=True)
    cd_geocodb = models.CharField(max_length=255, default=None, null=True, blank=True)
    nm_bairro = models.CharField(max_length=255, default=None, null=True, blank=True)
    cd_geocods = models.CharField(max_length=255, default=None, null=True, blank=True)
    nm_subdist = models.CharField(max_length=255, default=None, null=True, blank=True)
    cd_geocodd = models.CharField(max_length=255, default=None, null=True, blank=True)
    nm_distrit = models.CharField(max_length=255, default=None, null=True, blank=True)
    cd_geocodm = models.CharField(max_length=255, default=None, null=True, blank=True)
    nm_municip = models.CharField(max_length=255, default=None, null=True, blank=True)
    nm_micro = models.CharField(max_length=255, default=None, null=True, blank=True)
    nm_meso = models.CharField(max_length=255, default=None, null=True, blank=True)
    geo_type = models.CharField(max_length=255, default=None, null=True, blank=True)
    geom = models.MultiPolygonField(default=None, blank=True)

    def __str__(self):
        return self.cd_geocodi
