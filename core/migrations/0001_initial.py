# Generated by Django 4.2.2 on 2023-07-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('titulo', models.CharField(max_length=255)),
                ('post', models.TextField()),
            ],
        ),
    ]
