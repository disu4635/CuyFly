from django.urls import path
from .views import home, select_fly

urlpatterns = [
    path('', home, name='home'),
    path('select_fly/', select_fly, name='select_fly')
    # Agrega más URL según sea necesario
]