from django.urls import path
from task1.views import task1

urlpatterns = [
    path('', task1, name='task1'),
]
