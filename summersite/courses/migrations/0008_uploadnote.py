# Generated by Django 4.2 on 2023-04-25 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_course_instructor'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='e.g. Week 1 notes', max_length=100, verbose_name='Title of notes')),
                ('upload_time', models.DateTimeField(auto_now_add=True, verbose_name='Upload time')),
                ('document', models.FileField(upload_to='notes/', verbose_name='Document to be uploaded')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lecture', verbose_name='Lecture corresponds to the notes')),
            ],
        ),
    ]
