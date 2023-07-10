"""
URL configuration for gpt_form_tasks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task1.views import index, task1
from task2.views import create, edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('task1/', task1, name='task1'),
    path('task2/create/', create, name='task2_create'),
    path('task2/edit/<int:task_id>', edit, name='task2_edit'),
    path('task3/create/', create, name='task3_create'),
    # path('task2/edit/<int:task_id>', edit, name='task2_edit'),

]
