from django.shortcuts import HttpResponse, render


# Create your views here.
def planning(request):
    return render(request, "plan/planning.html")


def notes(request):
    return render(request, "plan/notes.html")


def tasks(request):
    return render(request, "plan/tasks.html")
