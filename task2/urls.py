from django.urls import path
from task2.views import create, edit
app_name = 'task2'

urlpatterns = [
    path('create/', create, name='create'),
    path('edit/<int:task_id>', edit, name='edit'),
]
