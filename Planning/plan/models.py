from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Task(models.Model):
    task_id=models.AutoField(primary_key=True)
    task_user=models.ForeignKey(User,on_delete=models.CASCADE)
    task_title=models.CharField(max_length=225)
    task_desc=models.TextField()
    task_dt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task_title}"
    
class Note(models.Model):
        note_id=models.AutoField(primary_key=True)
        note_user=models.ForeignKey(User,on_delete=models.CASCADE)
        note_title=models.CharField(max_length=225)
        note_body=models.TextField()
        note_dt=models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.note_title}"