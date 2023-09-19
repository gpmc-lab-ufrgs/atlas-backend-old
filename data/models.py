from django.db import models

from dictionary.models import Dictionary
from district.models import District
from state.models import State
from sectors.models import Sectors,SectorsSensus
from upload.models import Spreadsheet_register


class Data_state(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE,related_name="state")
    dictionary = models.ForeignKey(Dictionary,on_delete=models.CASCADE,related_name="dictionary")
    value = models.CharField(max_length=255,default=None,null=True,blank=True)
    Spreadsheet_register = models.ForeignKey(Spreadsheet_register, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.value + " - " + self.dictionary.name + " - " + self.state.name

class Data_city(models.Model):
    city = models.ForeignKey(District,on_delete=models.CASCADE,related_name="city")
    dictionary = models.ForeignKey(Dictionary,on_delete=models.CASCADE,related_name="dictionary_city")
    value = models.CharField(max_length=255,default=None,null=True,blank=True)
    Spreadsheet_register = models.ForeignKey(Spreadsheet_register, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.value + " - " + self.dictionary.name + " - " + self.city.name

class Data_sector(models.Model):
    sector = models.ForeignKey(SectorsSensus,on_delete=models.CASCADE,related_name="sector")
    dictionary = models.ForeignKey(Dictionary,on_delete=models.CASCADE,related_name="dictionary_sector")
    value = models.CharField(max_length=255,default=None,null=True,blank=True)
    Spreadsheet_register = models.ForeignKey(Spreadsheet_register, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.value + " - " + self.dictionary.name + " - " + self.sector.cd_geocodi

### CNAE ###

class Cnae(models.Model):
    cnae = models.CharField(max_length=255,blank=True, null=True)
    descricao = models.CharField(max_length=1000,blank=True, null=True)
    cod_setor = models.CharField(max_length=255,blank=True, null=True)
    nome_setor = models.CharField(max_length=1000,blank=True, null=True)
    Spreadsheet_register = models.ForeignKey(Spreadsheet_register, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.cnae

class Cnae_munic(models.Model):
    city = models.ForeignKey(District, on_delete=models.CASCADE, related_name="munic")
    cnae = models.ForeignKey(Cnae, on_delete=models.CASCADE, related_name="cnae_cod")
    total = models.CharField(max_length=255,blank=True, null=True)
    Spreadsheet_register = models.ForeignKey(Spreadsheet_register, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.cnae + " " + self.city + " " + self.total