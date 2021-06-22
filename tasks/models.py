from django.db import models
from django.db.models.deletion import CASCADE

class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=100, blank=True,null=True)
    
    def __str__(self):
        return self.title