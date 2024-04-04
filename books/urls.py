from django.urls import path
from .views import RegisterView,LoginView,LogoutView,ProfileUpdateView,category


app_name = 'books'

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/',ProfileUpdateView.as_view(),name='profile'),
    path('lang/<int:id>/',category,name='category'),
]