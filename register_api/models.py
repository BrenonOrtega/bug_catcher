from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Error(models.Model):
    OPEN = 'OPEN'
    EVALUATING = 'EVAL'
    SOLVED = 'SOLV'
    STATUS_CHOICES = [
        (OPEN, 'Em Aberto'),
        (EVALUATING, 'Em Avaliação'),
        (SOLVED, 'Solucionado')
    ]
    
    id = models.AutoField(primary_key=True)
    name = models.CharField("Nome do erro", max_length = 100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    email = models.EmailField("Email do usuário", max_length=100, blank=True)
    date = models.DateTimeField("data de criação",auto_now_add=True)
    last_update = models.DateTimeField("Ultima atualização", auto_now=True)
    description = models.TextField("Descrição do erro", blank=True)
    status = models.CharField(
        max_length = 20,
        blank=False,
        choices = STATUS_CHOICES,
        default = OPEN
    )

    class Meta:
        verbose_name_plural = "errors"

    def __str__(self):
        return "%s criado por %s" %(self.name, self.author)
