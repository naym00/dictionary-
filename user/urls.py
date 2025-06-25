from django.urls import path
from user import views

urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('set-password/', views.set_password, name='set-password'),
    path('logout/', views.user_logout, name='logout'),
    
    path('unique-username/<str:username>/', views.unique_username, name='unique-username'),
]
