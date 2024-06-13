from django.db import models
from django.db.models import F

class Note(models.Model):
    note = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    commend_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.note[:50]  # Return first 50 characters of note for display

class Command(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    command = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.command