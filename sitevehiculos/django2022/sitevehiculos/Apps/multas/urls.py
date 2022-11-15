from django.urls import path
from Apps.multas.views import MultaList, MultaDetail


app_name = "multas"

urlpatterns = [
    path('', MultaList.as_view()),
    path('<int:pk>', MultaDetail.as_view()),
]