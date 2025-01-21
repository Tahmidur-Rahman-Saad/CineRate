from django.urls import path
from . import views  

urlpatterns = [
    path('', views.movies, name='movies'),
    path('movie-details/<str:pk>/', views.movieDetails, name='movie-details'),
    path('movie-create/', views.movieCreate, name='movie-create'),
    path('movie-update/<str:pk>/', views.movieUpdate, name='movie-update'),
    path('movie-delete/<str:pk>/', views.movieDelete, name='movie-delete'),
    path('rating-set/<int:key>', views.ratingsSet, name='rating-set'),
    path('top-rated-movie-checking/<int:days>/<int:counts>/', views.movieTopRatingChecking, name='top-rated-movie-checking'),
    path('recent-release-music-checking/<int:days>/<int:counts>/', views.musicRecentReleaseChecking, name='recent-release-music'),
    path('musics/', views.musics, name='musics'),    
]
