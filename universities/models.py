from django.db import models
from django.contrib.auth.models import AbstractUser

class Applicant(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=70, unique=True, null=False)
    adress = models.TextField()
    number = models.CharField(max_length=15)


    def __str__(self):
        return self.username

class University(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=30)
    afiliated_to = models.CharField(max_length=100)
    adress = models.TextField()
    year_established = models.DateField()
    web_link = models.CharField(max_length=100)
    picture = models.ImageField()


    def __str__(self):
        return self.name

class Level(models.Model):
    level_name = models.CharField(max_length=20)    


    def __str__(self):
        return self.level_name


class Language(models.Model):
    Language_name = models.CharField(max_length=20)

    def __str__(self):
        return self.Language_name

class Course(models.Model):
    course_name =models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    credit = models.IntegerField()
    tuition_fee = models.IntegerField()
    period = models.CharField(max_length=100)
    date = models.DateField()
    language_of_instruction = models.ForeignKey(Language, on_delete=models.CASCADE)
    course_level = models.ForeignKey(Level, on_delete=models.CASCADE)
    link_to_couse_website = models.CharField(max_length=100)
    pace_of_study = models.FloatField()
    teaching_form = models.CharField(max_length=100)
    meetings = models.IntegerField()
    location = models.TextField()
    instruction_time = models.TimeField()
    image = models.ImageField()


    def __str__(self):
        return self.course_name
