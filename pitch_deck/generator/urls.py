from django.urls import path

from . import views

app_name = 'generator'

urlpatterns = [
    path('pitch-deck', views.pitch_deck, name='pitch-deck'),
    path('', views.index, name='index'),
]
