
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('components/', views.components, name='components')
]
