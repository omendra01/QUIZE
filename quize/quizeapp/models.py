from audioop import maxpp
from django.db import models

# Create your models here.

class QuizeQuestion(models.Model):
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class Register(models.Model):
    mobile = models.IntegerField()
    def __str__(self):
        return str(self.mobile)       