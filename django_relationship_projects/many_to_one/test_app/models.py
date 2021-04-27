from django.db import models

# Create your models here.

class student(models.Model):
    sname=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    age=models.IntegerField()

    def __str__(self):
        return self.sname

class cource(models.Model):
    #student=models.ForeignKey(student,on_delete=models.DO_NOTHING)
    student=models.ForeignKey(student,on_delete=models.SET_NULL,null=True)
    cname=models.CharField(max_length=20)
    fee=models.FloatField()

    def __str__(self):
        return self.cname