from django.urls import path
from Apps.vehiculos.views import VehiculoList, VehiculoDetail


app_name = "vehiculos"

urlpatterns = [
    path('', VehiculoList.as_view()),
    path('<int:pk>', VehiculoDetail.as_view()),
]