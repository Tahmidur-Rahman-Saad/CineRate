from django.urls import path
from . import views  

urlpatterns = [
    path('directors/', views.directors, name='directors'),
    path('casts/', views.casts, name='casts'),
    path('authorizers/', views.authorizers, name='authorizers'),

    path('director-details/<int:pk>/', views.directorDetails, name='director-details'),
    path('director-update/<int:pk>/', views.directorUpdate, name='director-update'),
    path('director-delete/<int:pk>/', views.directorDelete, name='director-delete'),
    path('director-create/', views.directorCreate, name='director-create'),

    path('cast-details/<int:pk>/', views.castDetails, name='cast-details'),
    path('cast-update/<int:pk>/', views.castUpdate, name='cast-update'),
    path('cast-delete/<int:pk>/', views.castDelete, name='cast-delete'),
    path('cast-create/', views.castCreate, name='cast-create'),

    path('authorizer-details/<int:pk>/', views.authorizerDetails, name='authorizer-details'),
    path('authorizer-update/<int:pk>/', views.authorizerUpdate, name='authorizer-update'),
    path('authorizer-delete/<int:pk>/', views.authorizerDelete, name='authorizer-delete'),
    path('authorizer-create/', views.authorizerCreate, name='authorizer-create'),

    path('reviewer-details/<int:pk>/', views.reviewerDetails, name='reviewer-details'),
    path('reviewer-update/<int:pk>/', views.reviewerUpdate, name='reviewer-update'),
    path('reviewer-delete/<int:pk>/', views.reviewerDelete, name='reviewer-delete'),
    path('reviewer-create/', views.reviewerCreate, name='reviewer-create'),

    path('login', views.logIn, name='login'),
    path('reset-password', views.resetPassword, name='reset-password'),
    
]
