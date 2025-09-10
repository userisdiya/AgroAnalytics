from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.login, name='login'),
    path("home/", views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]
