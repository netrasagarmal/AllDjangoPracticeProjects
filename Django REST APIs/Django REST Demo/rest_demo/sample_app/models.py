from pickle import TRUE
from django.db import models

class StudentModel(models.Model):
    sId = models.AutoField(primary_key=TRUE)
    studentName = models.CharField(max_length = 100)
    studentClass = models.IntegerField()
