# Generated by Django 4.2.2 on 2023-07-31 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_usuario_numero_de_tarjeta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='numero_de_tarjeta',
            field=models.IntegerField(null=True),
        ),
    ]
