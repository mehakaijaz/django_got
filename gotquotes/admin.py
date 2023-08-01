from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

class ActorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...
admin.site.register(Actor,ActorAdmin)

class QuoteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    ...
admin.site.register(Quote,QuoteAdmin)
