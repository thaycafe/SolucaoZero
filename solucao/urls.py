from django.urls import path
from .views import solucao
from .views import kba

urlpatterns = [
    path('', solucao, name='solucao'),
    path('kba', kba, name='kba')
]