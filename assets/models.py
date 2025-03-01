from django.db import models

class ITAsset(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    purchase_date = models.DateField()
    warranty_expiration = models.DateField()

    def __str__(self):
        return self.name

class SoftwareLicense(models.Model):
    asset = models.ForeignKey(ITAsset, on_delete=models.CASCADE)
    license_key = models.CharField(max_length=100, unique=True)
    expiration_date = models.DateField()

    def __str__(self):
        return self.license_key

class MaintenanceSchedule(models.Model):
    asset = models.ForeignKey(ITAsset, on_delete=models.CASCADE)
    maintenance_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'Maintenance for {self.asset.name} on {self.maintenance_date}'