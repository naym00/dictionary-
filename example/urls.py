from django.urls import path
from example import views

urlpatterns = [
    path('add-example/<int:word_id>/', views.add_example, name='add-example'),
    path('edit-example/<int:id>/', views.edit_example, name='edit-example'),
    path('delete-example/<int:id>/', views.delete_example, name='delete-example'),
]