from django.db import models

# Create your models here.
class Student(models.Model):
    Grade =(
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
    )

    firstname = models.CharField(max_Length=200, null=True)
    lastname = models.CharField(max_Length=200, null=True)
    middlename = models.CharField(max_Length=200, null=True)
    grade = models.CharField(max_Length=200, null=True, choices=Grade)

    def __str__(self) -> str:
        return ""+ str(self.lastname) + ", " + str(self.firstname)