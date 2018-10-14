from django.urls import path
from .views import home,medicao,calibrar

urlpatterns = [
    path('', home, name='home'),
    path('medicao', medicao, name='medicao'),
    path('calibrar',calibrar, name='calibrar')
]