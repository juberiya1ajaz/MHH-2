from django.db import models
from django.contrib.auth.models import User


class Diary(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    mood = models.CharField(max_length=10)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


