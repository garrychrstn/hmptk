from django.db import models

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
    desc = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} {self.date}"