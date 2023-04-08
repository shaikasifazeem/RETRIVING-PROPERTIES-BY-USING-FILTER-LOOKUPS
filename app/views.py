from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def D_NAME(request):
    DOT=DEPT.objects.all()
    # DOT=DEPT.objects.filter(DNAME__startswith='A')
    DOT=DEPT.objects.filter(DLOC__endswith='s')
    DOT=DEPT.objects.filter(DLOC__contains='a')

    DOT=DEPT.objects.filter(DLOC__contains='K')

    
    d={'DEPTS':DOT}
    return render(request,'display.html',context=d)

def E_NAME(request):
    EOT=EMP.objects.all()
    EOT=EMP.objects.filter(EMPNO__contains='2')
    EOT=EMP.objects.filter(ENAME__startswith='a')
    EOT=EMP.objects.filter(ENAME__startswith='s')
    EOT=EMP.objects.filter(ENAME__endswith='a')
    EOT=EMP.objects.filter(ENAME__endswith='n')
    EOT=EMP.objects.filter(ENAME__in=('ALLEN','MARTIN','WORD'))

    EOT=EMP.objects.all()
    EOT=EMP.objects.filter(ENAME__in=('ALLEN','MARTIN','WORD'))
    EOT=EMP.objects.filter(HIREDATE__month='12')
    EOT=EMP.objects.filter(HIREDATE__year='1981')
    EOT=EMP.objects.filter(HIREDATE__day='2')
    EOT=EMP.objects.filter(HIREDATE__startswith='1')
    EOT=EMP.objects.filter(HIREDATE__endswith='0')
    EOT=EMP.objects.filter(ESAL__in=('1250','1600'))
    EOT=EMP.objects.filter(ESAL__startswith='16')
    EOT=EMP.objects.filter(ESAL__endswith='0')
    EOT=EMP.objects.filter(ESAL__in=('1600','2975'))
    EOT=EMP.objects.all()
    EOT=EMP.objects.filter(ESAL__in=('1600','2975'))
    EOT=EMP.objects.filter(ESAL__lt='1700')
    EOT=EMP.objects.filter(ESAL__gte='1700')
    EOT=EMP.objects.filter(ESAL__lte='1700')
    EOT=EMP.objects.filter(COMM='0')
    EOT=EMP.objects.filter(DEPTNO__in=('20','30'))








    d={'EMPS':EOT}
    return render(request,'display1.html',context=d)