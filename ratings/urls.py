from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('see-ratings/',views.ratings),
    path('rating-details/<int:pk>/',views.ratingDetails),
    path('ratings-create/',views.ratingsCreate),
    path('ratings-update/<int:pk>/',views.ratingsUpdate),
    path('ratings-delete/<int:pk>/',views.ratingsDelete),
]