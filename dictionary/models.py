from django.db import models

from django.utils.translation import gettext_lazy as _
from upload.models import Spreadsheet_register

class Dictionary(models.Model):
    agency = models.CharField(max_length=255, default=None, null=True, blank=True)
    name = models.CharField(max_length=255, default=None, primary_key=True)
    id_sheet = models.CharField(max_length=255,  null=True, blank=True)
    description_en = models.TextField(default=None, null=True, blank=True)
    description_ptbr = models.TextField(default=None, null=True, blank=True)
    label_en = models.CharField(max_length=255, default=None, null=True, blank=True)
    label_ptbr = models.CharField(max_length=255, default=None, null=True, blank=True)
    unit = models.CharField(max_length=255,default=None, null=True, blank=True)
    format = models.CharField(max_length=255, null=True, blank=True,default='Int')
    new_classification_ptbr = models.CharField(max_length=255, default=None, null=True, blank=True)
    new_classification_en = models.CharField(max_length=255, default=None, null=True, blank=True)
    ranking = models.IntegerField(default=None, null=True, blank=True)
    table = models.CharField(max_length=255, default=None, null=True, blank=True)
    Spreadsheet_register = models.ForeignKey(Spreadsheet_register, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.name