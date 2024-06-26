from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('register/', views.RegisterView.as_view(), name='register'),  # Add this line for registration
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('learn/', views.learn, name='learn'),
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
]
