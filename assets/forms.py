from django import forms
from .models import ITAsset, SoftwareLicense, MaintenanceSchedule

class ITAssetForm(forms.ModelForm):
    class Meta:
        model = ITAsset
        fields = ['name', 'serial_number', 'purchase_date', 'warranty_expiration']

class SoftwareLicenseForm(forms.ModelForm):
    class Meta:
        model = SoftwareLicense
        fields = ['asset', 'license_key', 'expiration_date']

class MaintenanceScheduleForm(forms.ModelForm):
    class Meta:
        model = MaintenanceSchedule
        fields = ['asset', 'maintenance_date', 'description']