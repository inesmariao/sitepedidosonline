# Generated by Django 4.2.2 on 2023-06-15 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_categoria_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('imagen', models.ImageField(upload_to='marcas', verbose_name='Imagen')),
            ],
            options={
                'db_table': 'marca',
            },
        ),
    ]
