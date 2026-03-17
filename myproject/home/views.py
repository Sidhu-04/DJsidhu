from django.shortcuts import get_object_or_404, redirect, render
import time
from django.http import HttpResponse

from .forms import EmpForm
from .models import Employee,User,Student
from django.contrib.auth import authenticate, login, logout

# from django.contrib.auth import User #default user model(ie wihtout customisation)

# Create your views here.

from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.urls import reverse_lazy


def hello(request):
    hai="<h1>Welcone to Django</h1>"
    return HttpResponse(hai)

# def welco(request):
#     return render(request,'welcome.html')

def welco(request,age):
    name="rojin"
    # name=input("enter your name: ")
    time=10
    print("my age is",age)
    return render(request,'welcome.html',{'details':name,'t':time,'a':age})


# def Empreg(request):
#     frm=EmpForm()
#     return render(request,'regEmp.html',{'form':frm})

def Empreg(request):
    if request.method=="POST":
        form=EmpForm(request.POST)
        if form.is_valid():
            form.save()
            print("................")
            return HttpResponse("sucessfully saved")
        else:
            return HttpResponse("error occured")
    else:
        print("//////////////")
        frm=EmpForm()
        return render(request,'regEmp.html',{'form':frm})
    

def mystatic(request):
    return render(request,'mystatic.html')

def myhome(request):
    return render(request,'home.html')

# _______________list emp_____________

def emp_list(request):
    emp= Employee.objects.all()
    return render(request,'listemp.html',{'data':emp})


def emp_del(request,id):
    # print("primary key is:",id)
    emp= Employee.objects.get(id=id)
    emp.delete()
    # return HttpResponse("Delete Employee")
    return redirect('/list')       #to redirect


def emp_edit(request,i):
    data=get_object_or_404(Employee,pk=i)
    frm=EmpForm(instance=data)
    return render(request,'edit_emp.html',{'form':frm})

def emp_update(request,i):
    data=get_object_or_404(Employee,pk=i)
    if request.method=="POST":
        frm=EmpForm(request.POST,instance=data)
        if frm.is_valid():
            frm.save()
            return redirect('/list')


def stud_reg(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pwd=request.POST.get('password')
        eml=request.POST.get('email')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        num=request.POST.get('ph')
        addr=request.POST.get('address')

        User.objects.create_user(username=uname,password=pwd,email=eml,first_name=fname,
                                 last_name=lname,phone=num,address=addr,is_staff=False,
                                 is_active=True,is_superuser=False)
        return HttpResponse("User registered Sucessfully")
    return render(request,'stud_reg.html')




class StudentCreateView(CreateView):
    model=Student
    fields=['name','email','age']
    template_name='student_form.html'
    success_url='/student/'


class StudentListView(ListView):
    model=Student
    template_name='student_list.html'
    context_object_name='stud'

class StudentDeleteView(DeleteView):
    model=Student
    template_name='student_confirm_delete.html'
    success_url=reverse_lazy('student-list')


def user_login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(username=uname, password=pwd)
        if user is not None:
            if user.is_superuser == False and user.is_staff == False: #student login
                login(request, user)
                return redirect('/SS/shome')
            elif user.is_superuser==True and user.is_staff==True: #teacher login
                login(request, user)
                return HttpResponse("Admin Login Successful")
        else:
            return HttpResponse("Invalid Credentials, try again")
        
    return render(request, 'login.html')

class StudentUpdateView(UpdateView):
    model=Student
    fields=['name','email','age']
    template_name='student_form_edit.html'
    success_url=reverse_lazy('student-list')
    