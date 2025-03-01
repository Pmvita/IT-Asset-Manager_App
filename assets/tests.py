from django.test import TestCase
from .models import ITAsset

class ITAssetModelTest(TestCase):
    def setUp(self):
        ITAsset.objects.create(name="Test Asset", serial_number="12345", purchase_date="2023-01-01", warranty_expiration="2024-01-01")

    def test_asset_str(self):
        asset = ITAsset.objects.get(serial_number="12345")
        self.assertEqual(str(asset), "Test Asset") 