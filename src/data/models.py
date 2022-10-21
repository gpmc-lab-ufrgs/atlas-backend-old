from django.db import models

from dictionary.models import Dictionary

class Data(models.Model):
    region_id = models.IntegerField(
        default=None, 
        null=True, 
        blank=True,
    )
    
    class TypeOptions(models.TextChoices):
        STATE = "state"
        DISTRICT = "district"
        
    type = models.CharField(
        max_length=50,
        choices=TypeOptions.choices,
        default=TypeOptions.STATE,
    ) 
    
    name = models.CharField(
        max_length=255, 
        default=None, 
        null=True, 
        blank=True,
    )
    
    value = models.CharField(
        max_length=255, 
        default=None, 
        null=True, 
        blank=True,
    )
    
    dictionary = models.ForeignKey(
        Dictionary,
        on_delete=models.CASCADE,
        related_name="dictionary",
    )
    
    def __str__(self):
        return self.value + " - " + self.name