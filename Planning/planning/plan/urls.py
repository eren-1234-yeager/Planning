from django.contrib import admin
from django.urls import path

from plan import views

urlpatterns = [
    path("planning/",views.planning),
    path("notes/",views.notes),
    path("tasks/",views.tasks)
]