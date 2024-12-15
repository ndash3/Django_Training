from django.db import models

# Create your models here.


class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    roll = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    mark = models.IntegerField()

    def __str__(self):
        return f'{self.name}_{self.roll}'
