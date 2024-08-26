from django.urls import path
from .views import SongRecommendationView
from . import views

urlpatterns = [
    path('recommend/', SongRecommendationView.as_view(), name = 'song-recommendation'),
    path("", views.index, name="index"),
]