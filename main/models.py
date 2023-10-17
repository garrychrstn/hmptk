from django.db import models
from django.utils import timezone

class Message(models.Model):
    msg = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.msg}"

class Event(models.Model):
    img = models.CharField(max_length=200)
    cat = models.CharField(max_length=40, default='WORKSHOP')
    line = models.CharField(max_length=10, default='OFFLINE')
    title = models.CharField(max_length=50)
    date = models.DateField()
    link = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000)
    upt = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title} {self.date}"

class News(models.Model):
    img = models.CharField(max_length=200)
    title = models.CharField(max_length=30)
    topic = models.CharField(max_length=20)
    desc = models.CharField(max_length=1000)
    art = models.TextField(max_length=2000)
    upt = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f"{self.title}, {self.topic}"