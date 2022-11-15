from django.urls import path
from Apps.personas.views import PersonaList, PersonaDetail


app_name = "personas"

urlpatterns = [
    path('', PersonaList.as_view()),
    path('<int:pk>', PersonaDetail.as_view()),
]