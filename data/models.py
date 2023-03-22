from django.db import models

from dictionary.models import Dictionary
from state.models import State
from upload.models import Spreadsheet_register


class Data_state(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE,related_name="state")
    dictionary = models.ForeignKey(Dictionary,on_delete=models.CASCADE,related_name="dictionary")
    value = models.CharField(max_length=255,default=None,null=True,blank=True)
    Spreadsheet_register = models.ForeignKey(Spreadsheet_register, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.value + " - " + self.dictionary.name + " - " + self.state.name