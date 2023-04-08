from django.db import models

# Create your models here.
class DEPT(models.Model):
    DEPTNO=models.IntegerField(primary_key=True)
    DNAME=models.CharField(max_length=100)
    DLOC=models.CharField(max_length=100)
    def __str__(self):
        return self.DNAME

class EMP(models.Model):
    EMPNO=models.IntegerField(primary_key=True)
    ENAME=models.CharField(max_length=100)
    ESAL=models.IntegerField(default=2000)
    MGR=models.CharField(max_length=100)
    HIREDATE=models.DateField()
    COMM=models.IntegerField(null=True)
    DEPTNO=models.ForeignKey(DEPT,on_delete=models.CASCADE)
    def __str__(self):
        return self.ENAME
