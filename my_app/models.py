from django.db import models
from django.contrib.auth.models import User
class Document(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
class Textnotes(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=255, blank=True)
    text=models.TextField()

class Questions(models.Model):
    title=models.CharField(max_length=25)
    question=models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name=models.CharField(max_length=50)
    comment=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
