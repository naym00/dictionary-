from django.urls import path
from word import views

urlpatterns = [
    path('words/', views.words, name='words'),
    path('new-words/', views.new_words, name='new-words'),
    path('easy-words/', views.easy_words, name='easy-words'),
    path('medium-words/', views.medium_words, name='medium-words'),
    path('hard-words/', views.hard_words, name='hard-words'),
    path('word-details/', views.word_details, name='word-details'),
    path('add-word/', views.add_word, name='add-word'),
    path('edit-word/<int:id>/', views.edit_word, name='edit-word'),
    path('delete-word/<int:id>/', views.delete_word, name='delete-word'),
]
