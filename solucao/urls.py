from django.urls import path
from .views import solucao

urlpatterns = [
    path('', solucao, name='solucao')
]