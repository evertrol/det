from django.urls import path, include
from . import views


app_name = 'example'

urlpatterns = [
    path('', views.index, name='index'),
]
