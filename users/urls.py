from django.urls import path
from .views import RegisterView, LoginView, LogoutView, getUserView

urlpatterns =[
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user-view/', getUserView.as_view()),
    path('logout/', LogoutView.as_view()),
]