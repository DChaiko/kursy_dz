from django.urls import path, include
from django.contrib import admin
from login.views import LoginView, LogoutView, PasswordChangeView, UserPage



urlpatterns = [
    path('login/', LoginView.as_view(), name = 'login-page'),
    path('logout/', LogoutView.as_view(), name = 'logout-page'),
    path('pass_change/', PasswordChangeView.as_view(), name = 'pass-change'),
    path('userpage/', UserPage.as_view(), name = 'user-page'),
    
]


