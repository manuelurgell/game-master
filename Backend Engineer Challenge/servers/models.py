from django.db import models

class Server(models.Model):
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

