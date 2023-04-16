from django.db import models
from user.models import MyUser

class Course(models.Model):

    SUBJECT_CHOICES = [
        ('APBI', 'APBI'),
        ('APSC', 'APSC'),
        ('BIOL', 'BIOL'),
        ('CHEM', 'CHEM'),
        ('COMM', 'COMM'),
        ('COMR', 'COMR'),
        ('CPEN', 'CPEN'),
        ('CPSC', 'CPSC'),
        ('DCSI', 'DCSI'),
        ('ECON', 'ECON'),
        ('ELEC', 'ELEC'),
        ('EOSC', 'EOSC'),
        ('MATH', 'MATH'),
        ('MFRE', 'MFRE'),
        ('PHIL', 'PHIL'),
        ('PHYS', 'PHYS'),
        ('PSYC', 'PSYC'),
        ('SCIE', 'SCIE'),
        ('STAT', 'STAT'),
        ('VANT', 'VANT'),
        ('WRDS', 'WRDS'),
    ]

    TERM_CHOICES = [
        ('SPRING', 'Spring'),
        ('SUMMER', 'Summer'),
        ('FALL', 'Fall'),
    ]

    subject = models.CharField(
        max_length=4, 
        choices=SUBJECT_CHOICES, 
        help_text="Subject code, e.g. ECON.", 
        blank=False
        )
    course_number = models.CharField(
        max_length=3, 
        help_text="3-digits course number, e.g. 101.", 
        blank=False
        )
    start_date = models.DateField(help_text="Starting date of the term.")
    end_date = models.DateField(help_text="End date of the term.")
    term = models.CharField(
        max_length=6, 
        choices=TERM_CHOICES, 
        help_text="Season of the term, e.g. Fall.", 
        blank=False)
    section = models.CharField(
        max_length=20, 
        help_text="Section number, e.g. 202 or professor name. <strong>Leave it blank</strong> if there is only one section.", 
        blank=True
        )
    instructor = models.ForeignKey(
        MyUser, 
        limit_choices_to={'is_tutor': True},
        on_delete=models.CASCADE
        )
    #slug = models.SlugField()

    def course_year(self):
        return self.start_date.strftime("%Y")

    def __str__(self):
        return self.subject + self.course_number + " - " + self.course_year() + self.term.lower() + self.section


