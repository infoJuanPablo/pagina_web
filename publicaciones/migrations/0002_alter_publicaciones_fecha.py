# Generated by Django 4.2.2 on 2023-07-07 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicaciones',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]