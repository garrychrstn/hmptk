from django.db import models

class Message(models.Model):
    msg = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.msg}"
