# Generated by Django 5.0.2 on 2024-07-01 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegos', '0002_juego_descripcion_alter_juego_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='descripcion',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='juego',
            name='imagen',
            field=models.ImageField(upload_to='juegos/'),
        ),
    ]
