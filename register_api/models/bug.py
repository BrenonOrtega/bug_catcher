from django.contrib.auth import get_user
from django.db import models
from django.conf import Settings, settings
from django.urls import reverse
from rest_framework.fields import ReadOnlyField


# Create your models here.

class Bug(models.Model):
    OPEN = 'OPEN'
    EVALUATING = 'EVAL'
    SOLVED = 'SOLV'
    STATUS_CHOICES = [
        (OPEN, 'Em Aberto'),
        (EVALUATING, 'Em Avaliação'),
        (SOLVED, 'Solucionado')
    ]

    id = models.AutoField(primary_key=int)
    bug_name = models.CharField("Nome do bug", max_length = 100)
    date = models.DateTimeField("data de criação",auto_now_add =True)
    last_update = models.DateTimeField("Ultima Atualização", auto_now = True)
    description = models.TextField("Descrição do Bug", blank=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="Bug",
        on_delete=models.CASCADE
    ) 
    status = models.CharField(
        max_length = 20,
        blank=False,
        choices = STATUS_CHOICES,
        default = OPEN
    )

    class Meta:
        verbose_name_plural = "Bugs"

    def __str__(self):
        return f"{self.bug_name} criado por {self.author} em {self.date}, ultima atualização:{self.last_update}"
