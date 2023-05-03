from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render

from plan.models import Note, Task


# Create your views here.
def planning(request):
    return render(request, "plan/planning.html")


def notes(request):
        notes=Note.objects.filter(note_user=request.user)
        params={
        'notes':notes
        }
        return render(request, "plan/notesList.html",params)

def addNotes(request):
    if request.method=="POST":
        noteT=request.POST.get('noteTitle')
        noteD=request.POST.get('noteBody')
        note=Note(note_title=noteT,note_body=noteD,note_user=request.user)
        note.save()
        messages.success(request,"Note Added Successfully!")
        return redirect('/notes')

    return render(request,'plan/notes.html')

def viewNote(request,id):
    try:
        note=Note.objects.get(note_id=id)
        return render(request,'plan/viewNote.html',{'note':note})
    except:
        return redirect('/notes')

def tasks(request):
    if request.method=="POST":
        t_title=request.POST.get('title')
        t_desc=request.POST.get('desc')
        task=Task(task_user=request.user,task_title=t_title,task_desc=t_desc)
        task.save()
        messages.success(request,"Task Added Successfully!")  
    
    tasks=Task.objects.filter(task_user=request.user)   
    params={
        "tasks":tasks
    }      
    todel=request.GET.get('delete')
  
    if todel:
        messages.success(request,"Task deleted Successfully!")
        Task.objects.filter(task_id=todel).delete()

    return render(request, "plan/tasks.html",params)

def updatetasks(request):
    if request.method=="POST":
        id =request.POST.get('id')
        title=request.POST.get('etitle')
        desc=request.POST.get('edesc')

        t=Task.objects.get(task_id=id)
        t.task_title=title
        t.task_desc=desc
        t.save()
        
        messages.success(request,"Task updated successfully!")   
        return redirect('/tasks')
    return redirect('/tasks')
