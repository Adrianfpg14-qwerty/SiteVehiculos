from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personas/', include('Apps.personas.urls')),
    path('multas/', include('Apps.multas.urls')),
    path('vehiculos/', include('Apps.vehiculos.urls')),
]
