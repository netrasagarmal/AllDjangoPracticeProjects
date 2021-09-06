from django.db import models

# Create your models here.
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)

'''

The __str__(self) method should be defined in a way that is easy to read and outputs all the members of the class. 
This method is also used as a debugging tool when the members of a class need to be checked. 
The __str__ method is called when the following functions are invoked on the object and return a 
string: print()

'''
