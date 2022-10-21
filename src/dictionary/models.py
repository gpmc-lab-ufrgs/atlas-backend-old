from django.db import models

from django.utils.translation import gettext_lazy as _

class Dictionary(models.Model):
    name = models.CharField(
        max_length=255, 
        default=None, 
        primary_key=True
    )
    
    agency = models.CharField(
        max_length=255, 
        default=None, 
        null=True, 
        blank=True,
    )
    
    class FormatOptions(models.TextChoices):
        INT = "INT", _("INT")
        FLOAT2 = "FT2", _("FLOAT2")
        
    format = models.CharField(
        max_length=3,
        choices=FormatOptions.choices,
        default=FormatOptions.INT,
    ) 
    
    class ClassificationOptions(models.TextChoices):
        ECONOMY = "E", _("Econômica")
        DEMOGRAPHIC = "D", _("Demográfica")
        
    classification = models.CharField(
        max_length=1,
        choices=ClassificationOptions.choices,
        default=ClassificationOptions.ECONOMY,
    )
       
    description = models.TextField(
        default=None, 
        null=True, 
        blank=True,
    )
       
    label = models.CharField(
        max_length=255, 
        default=None, 
        null=True, 
        blank=True,
    )
    
    class UnitOptions(models.TextChoices):
        MONEY = "M", _("Money")
        NUMBER = "N", _("Number")
        DISTANCE = "D", _("Distance")
       
    unit = models.CharField(
        max_length=1,
        choices=UnitOptions.choices,
        default=UnitOptions.NUMBER,
    )
    
    def __str__(self):
        return self.name