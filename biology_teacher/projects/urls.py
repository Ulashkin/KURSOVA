from django.urls import path
from .views import register, projects_list, upload_project

urlpatterns = [
    path('register/', register, name='register'),
    path('projects/', projects_list, name='projects_list'),
    path('upload/', upload_project, name='upload_project'),
]