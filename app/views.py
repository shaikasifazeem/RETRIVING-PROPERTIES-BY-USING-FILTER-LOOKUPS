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


    DOT=DEPT.objects.all()


    
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
    EOT=EMP.objects.all()


    d={'EMPS':EOT}
    return render(request,'display1.html',context=d)
def update_display(request):
     DOT=DEPT.objects.filter(DNAME='ACCOUNTING').update(DNAME='ROHIT')
     DOT=DEPT.objects.filter(DNAME='OPERATIONS').update(DNAME='kohli')
     DOT=DEPT.objects.filter(DNAME='ROHIT').update(DNAME='ACCOUNTING')
     DOT=DEPT.objects.filter(DNAME='kohli').update(DNAME='OPERATIONS')
     DOT=DEPT.objects.filter(DLOC='BOSTON').update(DLOC='BUDILI')
     DOT=DEPT.objects.filter(DLOC='NEW YORK').update(DLOC='GORANTLA')
     D5=DEPT.objects.get_or_create(DEPTNO=50,DNAME='SOFTWARE',DLOC='BENGALORE')[0]
     D5.save()
     DOT=DEPT.objects.update_or_create(DEPTNO=50,DNAME='SOFTWARE',DLOC='BENGALORE',defaults={'DLOC':'HYDRABAD'})
     DOT=DEPT.objects.filter(DLOC='BENGALORE').update(DLOC='HYDRABAD')
     
     D6=DEPT.objects.get_or_create(DEPTNO=30,DNAME='SALES',DLOC='CHICAGO')[0]
     D6.save()
     DOT=DEPT.objects.update_or_create(DLOC='GORANTLA',defaults={'DLOC':'NEW YOURK'})

     return render(request,'display.html')
def delete(request):
    DOT=DEPT.objects.filter(DEPTNO=50).delete()
    DOT=DEPT.objects.filter(DNAME='SALES').delete()
    return render(request,'display.html')
def update_emp(request):

    EOT=EMP.objects.filter(ENAME='JONES').update(ENAME='ASIF')
    EOT=EMP.objects.filter(ENAME='SMITH').update(ENAME='AZEEM')
    D6=DEPT.objects.get_or_create(DEPTNO=30,DNAME='SALES',DLOC='CHICAGO')[0]
    D6.save()

    E5=EMP.objects.get_or_create(EMPNO=7499,ENAME='ALLEN',ESAL=1600,MGR	='7698',HIREDATE='1981-02-20',COMM=300,DEPTNO=D6)[0]
    E5.save()


    # EOT=EMP.objects.all()

    return render(request,'display1.html')


