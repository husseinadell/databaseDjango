from django.db import models

# Create your models here.


class User(models.Model):
    name=models.CharField(max_length=150)
    mobile=models.CharField(max_length=20)
    password=models.CharField(max_length=15)
    def __str__(self):
        return (self.name)

class PstTests(models.Model):
    user_name =models.ForeignKey(User)
    result=models.IntegerField()
    testNumber=models.IntegerField()

    def __str__(self):
        return str(self.testNumber)

class Questions(models.Model):
    test = models.ForeignKey(PstTests)
    q_type =models.CharField(max_length=30)
    answer =models.CharField(max_length=30)
    degree =models.IntegerField()

    def __str__(self):
        return (self.q_type)
