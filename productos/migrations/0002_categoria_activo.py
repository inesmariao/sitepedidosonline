# Generated by Django 4.2.2 on 2023-06-10 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
    ]
