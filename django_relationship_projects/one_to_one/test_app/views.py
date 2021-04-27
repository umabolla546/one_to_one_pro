from django.shortcuts import render
from .models import student,cource
from django.db.models import Count

# Create your views here.

def view_fun(request):
    #stu=cource.objects.all()

    stu=student.objects.all().annotate(c_count=Count('cource'))
    #return render(request,'student.html',{'stu':stu})
    return render(request,'student1.html',{'stu':stu})