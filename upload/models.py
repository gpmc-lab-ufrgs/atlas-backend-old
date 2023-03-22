from django.db import models
from django.contrib.auth.models import User

class Spreadsheet_register(models.Model):
    Id = models.AutoField(primary_key=True, unique=True)
    Sheet_name = models.TextField('Sheet_name', blank=True, null=True)
    Date = models.DateField('Date', blank=True, null=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Spreadsheet_register'
        verbose_name_plural = 'Spreadsheet_register'

        def __str__(self):
            return self.Id