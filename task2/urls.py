from django.urls import path
from task2.views import create, edit

urlpatterns = [
    path('create/', create, name='task2_create'),
    path('edit/<int:task_id>', edit, name='task2_edit'),
]
