from django.urls import path
from settings import views

urlpatterns = [
    path('get-settings/', views.get_settings, name='get-settings'),
    # path('edit-example/<int:id>/', views.edit_example, name='edit-example'),
    # path('delete-example/<int:id>/', views.delete_example, name='delete-example'),
]