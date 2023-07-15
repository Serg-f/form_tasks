from django.urls import path
from task3.views import create

urlpatterns = [
    path('create/', create, name='task3_create'),
    # path('edit/<int:task_id>', edit, name='task2_edit'),
]
