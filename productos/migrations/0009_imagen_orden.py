# Generated by Django 4.2.2 on 2023-06-15 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0008_alter_imagen_options_remove_imagen_imagen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagen',
            name='orden',
            field=models.IntegerField(default=1, verbose_name='Orden'),
            preserve_default=False,
        ),
    ]
