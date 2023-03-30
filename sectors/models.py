from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Sectors(models.Model):
    cd_setor = models.CharField(max_length=15)
    cd_sit = models.CharField(max_length=1,default=None,null=True,blank=True)
    nm_sit = models.CharField(max_length=50,default=None,null=True,blank=True)
    cd_uf = models.CharField(max_length=2,default=None,null=True,blank=True)
    nm_uf = models.CharField(max_length=50,default=None,null=True,blank=True)
    sigla_uf = models.CharField(max_length=2,default=None,null=True,blank=True)
    cd_mun = models.CharField(max_length=7,default=None,null=True,blank=True)
    nm_mun = models.CharField(max_length=60,default=None,null=True,blank=True)
    cd_dist = models.CharField(max_length=9,default=None,null=True,blank=True)
    nm_dist = models.CharField(max_length=100,default=None,null=True,blank=True)
    cd_subdist = models.CharField(max_length=11,default=None,null=True,blank=True)
    nm_subdist = models.CharField(max_length=100,default=None,null=True,blank=True)
    geom = models.MultiPolygonField(default=None,blank=True)

    def __str__(self):
        return self.cd_setor
