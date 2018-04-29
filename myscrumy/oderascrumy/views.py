from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    target = ScrumyGoals.objects.exclude(goal_type ='daily goals')
    return HttpResponse(target)

def goals(request,pk):
    goal = ScrumyGoals.objects.all()
    return HttpResponse(goal)

def move_goals(request, task_id):
    task=ScrumyGoals.objects.get(id=task_id)
    return HttpResponse(task.description)

def add_user(request):
    add=ScrumyUser.objects.create(name='debbie',location='lagos',email='debbieyahoo.com',roles='')
    add.save()
    users=ScrumyUser.objects.all()
    for names in users:
        pass
    return HttpResponse(users)
