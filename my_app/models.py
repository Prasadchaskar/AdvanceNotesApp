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
