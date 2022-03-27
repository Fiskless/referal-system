from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('users/create/phone', views.UserAuthorizationView.as_view()),
    path('users/create/auth_code', views.AuthCodeView.as_view()),
    path('users/<int:pk>/', views.UserView.as_view()),
    # path('users/create/auth_code', views.login),
]
