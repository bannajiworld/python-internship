from django.db import models

# Create your models here.
class person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)

    def __str__(self):
        return self.first_name, self.last_name

class student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    gender=models.BooleanField(default=False)

    fees=models.IntegerField()

    def __str__(self):
        return self.first_name



 