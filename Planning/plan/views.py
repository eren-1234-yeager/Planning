from django.contrib.messages import constants as messages
from django.shortcuts import HttpResponse, render

from plan.models import Task


# Create your views here.
def planning(request):
    return render(request, "plan/planning.html")


def notes(request):
    return render(request, "plan/notes.html")


def tasks(request):
    if request.method=="POST":
        t_title=request.POST.get('title')
        t_desc=request.POST.get('desc')
        task=Task(task_user=request.user,task_title=t_title,task_desc=t_desc)
        task.save()
        messages.success(request,"Task Added Successfully!")            
    return render(request, "plan/tasks.html")
