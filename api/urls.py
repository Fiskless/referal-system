from django.urls import path

from . import views

urlpatterns = [
    path('users/create/', views.UserAuthorizationView.as_view()),
    path('users/<int:pk>/', views.UserView.as_view()),
]
