from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length = 100)
    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField
    STATUS_CHOICES = [
        ('OPEN', 'Em Aberto'),
        ('BUSY', 'Em Processo'),
        ('SOLVED', 'Solucionado')
    ]
    status = models.CharField(
        max_length = 7,
        choices = STATUS_CHOICES,
        default = 'OPEN'
    )

    def __str__(self):
        return self.name

