from django.shortcuts import render, redirect, get_object_or_404
from .models import ITAsset
from .forms import ITAssetForm

def asset_list(request):
    assets = ITAsset.objects.all()
    return render(request, 'assets/asset_list.html', {'assets': assets})

def add_asset(request):
    if request.method == 'POST':
        form = ITAssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    else:
        form = ITAssetForm()
    return render(request, 'assets/add_asset.html', {'form': form})

def edit_asset(request, asset_id):
    asset = get_object_or_404(ITAsset, id=asset_id)
    if request.method == 'POST':
        form = ITAssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    else:
        form = ITAssetForm(instance=asset)
    return render(request, 'assets/edit_asset.html', {'form': form, 'asset': asset})

def delete_asset(request, asset_id):
    asset = get_object_or_404(ITAsset, id=asset_id)
    if request.method == 'POST':
        asset.delete()
        return redirect('asset_list')
    return render(request, 'assets/delete_asset.html', {'asset': asset})