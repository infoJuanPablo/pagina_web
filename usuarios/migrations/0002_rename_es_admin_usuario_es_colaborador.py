# Generated by Django 4.2.2 on 2023-07-20 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='es_admin',
            new_name='es_colaborador',
        ),
    ]
