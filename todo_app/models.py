from django.db import models

# Create your models here.
class Todo_list(models.Model):
    task_name=models.CharField(max_length=200)
    desc=models.TextField()
    priority=models.IntegerField()
    date=models.DateField()
    def __str__(self):
        return self.task_name

