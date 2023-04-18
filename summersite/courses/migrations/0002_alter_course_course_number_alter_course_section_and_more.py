# Generated by Django 4.2 on 2023-04-16 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_number',
            field=models.CharField(help_text='3-digits course number, e.g. 101.', max_length=3),
        ),
        migrations.AlterField(
            model_name='course',
            name='section',
            field=models.CharField(blank=True, help_text='Section number, e.g. 202. Leave it blank if there is only one section.', max_length=3),
        ),
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.CharField(choices=[('APBI', 'APBI'), ('APSC', 'APSC'), ('BIOL', 'BIOL'), ('CHEM', 'CHEM'), ('COMM', 'COMM'), ('COMR', 'COMR'), ('CPEN', 'CPEN'), ('CPSC', 'CPSC'), ('DCSI', 'DCSI'), ('ECON', 'ECON'), ('ELEC', 'ELEC'), ('EOSC', 'EOSC'), ('MATH', 'MATH'), ('MFRE', 'MFRE'), ('PHIL', 'PHIL'), ('PHYS', 'PHYS'), ('PSYC', 'PSYC'), ('SCIE', 'SCIE'), ('STAT', 'STAT'), ('VANT', 'VANT'), ('WRDS', 'WRDS')], help_text='subject code, e.g. ECON.', max_length=4),
        ),
        migrations.AlterField(
            model_name='course',
            name='term',
            field=models.CharField(choices=[('SPRING', 'SPRING'), ('SUMMER', 'SUMMER'), ('FALL', 'FALL')], help_text='Season of the term.', max_length=6),
        ),
    ]