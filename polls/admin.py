from django.contrib import admin
from . import models


@admin.register((models.user))
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.report)
class ReportAdmin(admin.ModelAdmin):
    pass
