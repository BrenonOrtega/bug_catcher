# Generated by Django 3.1.6 on 2021-02-08 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_api', '0003_auto_20210207_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='error',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descrição do erro'),
        ),
    ]