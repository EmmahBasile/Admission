from django.contrib import admin
from  . models import University, Applicant, Level, Language, Course
# Register your models here.

admin.site.register(University)
admin.site.register(Applicant)
admin.site.register(Level)
admin.site.register(Course)
admin.site.register(Language)