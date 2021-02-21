# Generated by Django 3.1.6 on 2021-02-07 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register_api', '0002_register_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome do erro')),
                ('slug', models.SlugField()),
                ('email', models.EmailField(max_length=100, verbose_name='Email do usuário')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='data de criação')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Ultima atualização')),
                ('status', models.CharField(choices=[('OPEN', 'Em Aberto'), ('EVAL', 'Em Avaliação'), ('SOLV', 'Solucionado')], default='OPEN', max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'errors',
            },
        ),
        migrations.DeleteModel(
            name='register',
        ),
    ]