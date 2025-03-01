from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('assets/', include('assets.urls')),
    path('', RedirectView.as_view(url='/assets/', permanent=True)),  # Redirect root to /assets/
] 