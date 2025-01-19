from django.urls import path
from . import views  

urlpatterns = [
    path('', views.movies, name='movies'),
    path('movie-details/<str:pk>/', views.movieDetails, name='movie-details'),
    path('movie-create/', views.movieCreate, name='movie-create'),
    path('movie-update/<str:pk>/', views.movieUpdate, name='movie-update'),
    path('movie-delete/<str:pk>/', views.movieDelete, name='movie-delete'),
    path('movie-search/<str:pk>/', views.movieSearch, name='movie-search'),
    path('movie-top-10-rating-last-week/', views.movieTopTenRatingLastWeek, name='movie-top-10-rating-last-week'),
    path('movie-top-10-rating-last-month/', views.movieTopTenRatingLastMonth, name='movie-top-10-rating-last-month'),
    path('movie-top-10-rating-last-year/', views.movieTopTenRatingLastYear, name='movie-top-10-rating-last-year'),
    path('movie-search-by-language/', views.movieSearchByLanguage, name='movie-search-by-language'),
    
]
