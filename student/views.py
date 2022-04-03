
from django.shortcuts import render,redirect
from django.http import HttpResponse


from django.contrib.auth.decorators import login_required

from student.models import student

# Create your views here.
def addstudent(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        rollno = request.POST['rollno']
        email = request.POST['email']
        dept= request.POST['dept']
        gender= request.POST['gender']
        number= request.POST['number']
        obj=student(
        firstname=firstname,
        lastname=lastname,
        id=rollno,
        email=email,
        department= dept,
        gender= gender,
        phoneNumber=number)
        obj.save()
        return redirect("index")
    return render(request,"add_student.html")