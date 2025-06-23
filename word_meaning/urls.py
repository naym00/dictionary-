from django.urls import path
from word_meaning import views

urlpatterns = [
    path('add-word-meaning/<int:word_id>/', views.add_word_meaning, name='add-word-meaning'),
    path('edit-word-meaning/<int:id>/', views.edit_word_meaning, name='edit-word-meaning'),
    path('delete-word-meaning/<int:id>/', views.delete_word_meaning, name='delete-word-meaning'),
]
