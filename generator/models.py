from django.db import models

# Create your models here.

class Presets(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField('date of creation')
    git_repo = models.CharField(max_length=100, default="no repo")

class Stack(models.Model):
    preset = models.ForeignKey(Presets, on_delete=models.CASCADE)
    languages = models.CharField(max_length=200)
