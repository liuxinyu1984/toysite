# Generated by Django 4.2 on 2023-04-11 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_tutor',
            field=models.BooleanField(default=False),
        ),
    ]
