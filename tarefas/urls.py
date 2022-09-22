from django.urls import path
from . import views
urlpatterns = [
   path('tasks/',views.tasks,name="tasks"),
   path('users/',views.users,name="users"),
   path('projects/',views.projects,name="projects"),
]