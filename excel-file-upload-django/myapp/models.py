from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name
