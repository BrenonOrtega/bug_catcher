# Generated by Django 3.1.6 on 2021-02-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_api', '0004_error_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='error',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
