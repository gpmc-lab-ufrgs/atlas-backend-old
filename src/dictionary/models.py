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
        INT = "INT"
        FLOAT2 = "FLOAT2"
        GRAPHIC = "GRAPHIC"
        PROGRESS_BAR = "PROGRESS_BAR"
        STRING = "STRING"
        
    format = models.CharField(
        max_length=12,
        choices=FormatOptions.choices,
        default=FormatOptions.INT,
    ) 
    
    class ClassificationOptions(models.TextChoices):
        HEALTH = "Sa", _("Saúde")
        EDUCATION = "Ed", _("Educação")
        ECONOMY = "Ec", _("Economia")
        MOBILITY = "Mo", _("Mobilidade")
        DEMOGRAPHIC = "De", _("Demografia")
        ENVIRONMENT = "Me", _("Meio Ambiente")
        URBANISM = "Ur", _("Urbanismo")
        SECURITY = "Se", _("Segurança")
        ENTREPRENEURSHIP = "Em", _("Empreendedorismo")
        TECNOLOGY = "Te", _("Tecnologia")
        
    classification = models.CharField(
        max_length=2,
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
        PORCENTAGE = "P", _("Porcentage")
        SQUARE_KILOMETERS = "K2", _("Square Kilometers")
        WAGES = "W", _("Wages")
        INHABITANT_KILOMETERS = "H", _("InhabitantKilometers")
        MBPS = "MB", _("MBPS")
       
    unit = models.CharField(
        max_length=2,
        choices=UnitOptions.choices,
        default=UnitOptions.NUMBER,
    )
    
    def __str__(self):
        return self.name