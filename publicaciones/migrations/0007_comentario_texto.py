# Generated by Django 4.2.2 on 2023-07-14 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0006_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='texto',
            field=models.TextField(null=True),
        ),
    ]
