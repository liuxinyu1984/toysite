# Generated by Django 4.2 on 2023-04-24 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_course_number_alter_course_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(help_text='Year of the term, e.g. 2023', max_length=4, verbose_name='Year')),
                ('season', models.CharField(choices=[('SPRING', 'Spring'), ('SUMMER', 'Summer'), ('FALL', 'Fall')], help_text='Season of the term, e.g. Fall.', max_length=6, verbose_name='Season')),
                ('start_date', models.DateField(help_text='Start date of the term.', verbose_name='Start Date')),
                ('end_date', models.DateField(help_text='End date of the term.', verbose_name='End Date')),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='term',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='slug',
        ),
        migrations.AlterField(
            model_name='lecture',
            name='course',
            field=models.ForeignKey(help_text='Select the course.', on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Course'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='is_final',
            field=models.BooleanField(default=False, help_text='Is this a final review lecture?', verbose_name='Final Review?'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='is_midterm',
            field=models.BooleanField(default=False, help_text='Is this a midterm review lecture?', verbose_name='Midterm Review?'),
        ),
    ]