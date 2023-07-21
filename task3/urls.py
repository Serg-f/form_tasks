from django.urls import path
from task3.views import create, edit
app_name = 'task3'

urlpatterns = [
    path('create/', create, name='create'),
    path('edit/<int:priority_id>', edit, name='edit')
]
