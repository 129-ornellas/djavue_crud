from django.shortcuts import render

from django.http import JsonResponse
from .models import Tasks, Users, Projects
# Create your views here.



def tasks(request):
    data = list(Tasks.objects.values())
    return JsonResponse(data,safe=False)

def users(request):
    data = list(Users.objects.values())
    return JsonResponse(data,safe=False)
   
def projects(request):
    data = list(Projects.objects.values())
    return JsonResponse(data,safe=False)
    