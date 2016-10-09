from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

class Challenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # add more things here

    def __str__(self):
        return self.user.username

class Challenge(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=3000)
    summary = models.CharField(max_length=200)
    slug = models.SlugField()
    challenger = models.ForeignKey(Challenger, on_delete=models.CASCADE)
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ChallengeAdmin(admin.ModelAdmin):
        prepopulated_fields = {"slug": ("name",)}

class Submission(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=3000)
    submitter = models.ForeignKey(Challenger, on_delete=models.CASCADE)
    # somehow include some data, or source code, or something?
    artifacts = models.FileField(null=True)
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
