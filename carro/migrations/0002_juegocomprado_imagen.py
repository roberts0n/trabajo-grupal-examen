# Generated by Django 5.0.2 on 2024-07-01 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='juegocomprado',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='juegos_comprados'),
        ),
    ]
