# Generated by Django 4.2.2 on 2023-08-03 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_alter_usuario_imagen_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='numero_de_tarjeta',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='imagen_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='imagen_perfil'),
        ),
    ]
