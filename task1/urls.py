from django.urls import path
from task1.views import task1
app_name = 'task1'

urlpatterns = [
    path('', task1, name='form1'),
]
