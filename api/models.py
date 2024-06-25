from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    commend_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.note[:50]

class LikeOrDislike(models.Model):
    LIKE = 'like'
    DISLIKE = 'dislike'
    TYPE_CHOICES = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_dislikes')
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='likes_dislikes')
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)

    class Meta:
        unique_together = ('user', 'note')
        verbose_name = "Like or Dislike"
        verbose_name_plural = "Likes or Dislikes"

    def __str__(self):
        return f"{self.id}--{self.user.username} {self.get_type_display()}d {self.note.note[:50]}"
    

class Command(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    command = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.command
