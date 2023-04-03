from django.shortcuts import render
from django.http import HttpResponse
from company.models import *

# Create your views here.

def dept(request):
    d_id=int(input('Enter Dept id: '))
    d_name=input('Enter department name: ')
    hr=departments.objects.get_or_create(dept_id=d_id,dname=d_name)[0]
    hr.save()
    return HttpResponse('Data inserted successfully in dept...!')



def emp(request):
    e_id=int(input('Enter Emp id: '))
    e_name=input('Enter Employee name: ')
    e_age=int(input('Enter Emp Age: '))
    #e_dept=input('Enter Employee dept name: ')
    d_id=int(input('Enter Dept id: '))
    d_name=input('Enter department name: ')
    hr=departments.objects.get_or_create(dept_id=d_id,dname=d_name)[0]
    hr.save()
    Emp1=employe.objects.get_or_create(emp_id=e_id,ename=e_name,age=e_age,dept=hr)[0]
    Emp1.save()
    return HttpResponse('Data inserted successfully in emp...!')