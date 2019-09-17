from django.contrib import admin
from .models import CuriculumVitae
from import_export.admin import ImportExportModelAdmin
# Register your models here.

# admin.site.register(CuriculumVitae)
@admin.register(CuriculumVitae)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id',)