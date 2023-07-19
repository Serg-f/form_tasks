from django.urls import path
from task3.views import create, edit

urlpatterns = [
    path('create/', create, name='task3_create'),
    path('edit/<int:priority_id>', edit, name='task3_edit')
]
