from django.contrib import admin
from .models import ITAsset, SoftwareLicense, MaintenanceSchedule

admin.site.register(ITAsset)
admin.site.register(SoftwareLicense)
admin.site.register(MaintenanceSchedule) 