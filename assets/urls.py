from django.urls import path
from .views import asset_list, add_asset, edit_asset, delete_asset

urlpatterns = [
    path('', asset_list, name='asset_list'),
    path('add/', add_asset, name='add_asset'),
    path('edit/<int:asset_id>/', edit_asset, name='edit_asset'),
    path('delete/<int:asset_id>/', delete_asset, name='delete_asset'),
] 