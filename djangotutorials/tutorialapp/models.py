from django.db import models

# Create your models here.
class Student(models.Model):
    Grade =(
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
    )

    firstname = models.CharField(max_length=200, null=True, verbose_name="First name ")
    lastname = models.CharField(max_length=200, null=True,verbose_name="Last name ")
    middlename = models.CharField(max_length=200, null=True,verbose_name="Middle name ")
    grade = models.CharField(max_length=200, null=True, choices=Grade,verbose_name="Grade ")

    def __str__(self) -> str:
        return ""+ str(self.lastname) + ", " + str(self.firstname) + ": " + str(self.grade)

class Teacher(models.Model):
    
    firstname = models.CharField(max_length=200, null=True, verbose_name="First name ")
    lastname = models.CharField(max_length=200, null=True, verbose_name="Last name ")
    classtype = models.CharField(max_length=200, null=True, verbose_name="Class type ")
    roomnumber = models.CharField(max_length=200, null=True, verbose_name="Room Number ")

    def __str__(self) -> str:
        return ""+ str(self.lastname) + ", " + str(self.firstname) + " is in room number: " + str(self.roomnumber)
