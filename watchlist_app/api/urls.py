from django.urls import path, include
from watchlist_app.api.views import Movie_list, Movie_details

urlpatterns = [
    path('list/', Movie_list, name='movie-list'),
    path('<int:pk>', Movie_details, name='movie-detail'),
]