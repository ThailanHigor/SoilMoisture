from django.urls import path
from .views import home,medicao

urlpatterns = [
    path('', home, name='home'),
    path('medicao', medicao, name='medicao')
]