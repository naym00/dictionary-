from django.contrib import admin
from django.urls import path, include
from dictionary import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('word/', include('word.urls')),
    path('word-meaning/', include('word_meaning.urls')),
    path('example/', include('example.urls')),
    path('settings/', include('settings.urls')),
]
