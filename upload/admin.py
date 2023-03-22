from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

@admin.register(Spreadsheet_register)
class Spreadsheet_registerAdmin(ImportExportModelAdmin):
    list_display = ('Id', 'Sheet_name', 'Date', 'User')