from django.contrib import admin

from .models import Projects, Users, Tasks

admin.site.register(Projects)
admin.site.register(Users)
admin.site.register(Tasks)
