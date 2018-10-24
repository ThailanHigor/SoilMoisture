from django.urls import path
from .views import home,medicao,calibrar,calculaPeso

urlpatterns = [
    path('', home, name='home'),
    path('medicao', medicao, name='medicao'),
    path('calibrar',calibrar, name='calibrar'),
    path('calcula_peso',calculaPeso, name='calculaPeso'),
]