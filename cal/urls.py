from . import views
from django.urls import path

app_name = 'cal'
urlpatterns = [
    path('', views.index, name='index'),
]
