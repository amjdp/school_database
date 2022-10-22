from django.db import models

# Create your models here.
class TeacherLogin(models.Model):
    teacher_email = models.CharField(max_length = 30)   # varchar(25)
    teacher_password = models.CharField(max_length = 20)