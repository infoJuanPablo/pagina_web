# Generated by Django 4.2.2 on 2023-08-03 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_alter_usuario_numero_de_tarjeta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='media.imagen_perfil'),
        ),
    ]
