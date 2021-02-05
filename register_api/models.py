from django.db import models

# Create your models here.

class register(models.Model):
    name = models.CharField(max_length = 100)
    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

