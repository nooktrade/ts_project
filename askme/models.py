from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_answer', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Answer by {self.answered_by.username}'
