from django.db import models

# Create your models here.
class StudentLogin(models.Model):
    s_id = models.CharField(max_length = 25)   # varchar(25)
    s_pwd = models.CharField(max_length = 30)