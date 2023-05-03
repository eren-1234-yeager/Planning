from django.contrib import admin
from django.urls import path

from plan import views

urlpatterns = [
    path("planning/",views.planning),

    path("notes/",views.notes),
    path("notes/add/",views.addNotes),
    path("notes/<str:id>/",views.viewNote),

    path("tasks/",views.tasks),
    path("tasks/update/",views.updatetasks),
    
]