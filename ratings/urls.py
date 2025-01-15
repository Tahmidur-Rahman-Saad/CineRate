from django.contrib import admin
from django.urls import path
from .views import ratings,ratingDetails,ratingsCreate,ratingsUpdate,ratingsDelete

urlpatterns = [
    path('see-ratings/',ratings),
    path('rating-details/<str:pk>/',ratingDetails),
    path('ratings-create/',ratingsCreate),
    path('ratings-update/<str:pk>/',ratingsUpdate),
    path('ratings-delete/<str:pk>/',ratingsDelete),
]