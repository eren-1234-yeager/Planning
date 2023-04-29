from django.shortcuts import HttpResponse, render

# Create your views here.


def index(request):
    return render(request,"home/index.html")

def about(request):
    return render(request,"home/about.html")
