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
    name = models.CharField("Nome do erro", max_length = 100)
    slug = models.SlugField(editable=False, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField("Email do usuário", max_length=100)
    date = models.DateTimeField("data de criação",auto_now_add=True)
    last_update = models.DateTimeField("Ultima atualização", auto_now=True)
    description = models.TextField("Descrição do erro", blank=True)
    status = models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = OPEN
    )

    class Meta:
        verbose_name_plural = "errors"

    def __str__(self):
        return "%s criado por %s" %(self.name, self.author)

    def get_absolute_url(self):
        return reverse('error_detail', kwargs={'slug: self.slug'})

