from django.shortcuts import render,redirect
from .models import *
from .forms import StudentsForm,TeacherForm,ScienceForm
def index(request):
    number = Student.objects.count()
    return render(request=request,template_name='crm_app/index.html',context={'number':number})
# Student section
def student(request):
    students = Student.objects.all()
    number = Student.objects.count()
    return render(request=request,template_name='crm_app/students.html',context={'students':students,'number':number})

def add_student(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')
        else: return redirect('add_student')
    form = StudentsForm
    return render(request=request,template_name='crm_app/add_student.html',context={'form':form})

def delete_student(request,id=None):
    if id:
        student = Student.objects.get(id=id)
        student.delete()
    return redirect('student')

def update_student(request, id=None):
    
    if id and request.method == 'POST':
        student = Student.objects.get(id=id)
        form = StudentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')
    else:
        if id:
            student = Student.objects.get(id=id)
            form = StudentsForm(instance=student)
        else:
            form = StudentsForm()

    return render(request=request, template_name='crm_app/update_student.html', context={'form': form})  
# Science section
def science(request):
    sciences = Science.objects.all()
    return render(request=request,template_name='crm_app/science.html',context={'sciences':sciences})

def add_science(request):
    if request.method == 'POST':
        form = ScienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('science')
        else: return redirect('add_science')
    form = ScienceForm
    return render(request=request,template_name='crm_app/add_sciense.html',context={'form':form})

def delete_science(request,id=None):
    if id:
        science = Science.objects.get(id=id)
        science.delete()
    return redirect('science')

def update_science(request, id=None):
    
    if id and request.method == 'POST':
        science = Science.objects.get(id=id)
        form = ScienceForm(request.POST, instance=science)
        if form.is_valid():
            form.save()
            return redirect('science')
    else:
        if id:
            student = Science.objects.get(id=id)
            form = ScienceForm(instance=student)
        else:
            form = ScienceForm()

    return render(request=request, template_name='crm_app/update_science.html', context={'form': form})
# Teacher section
def teacher(request):
    teachers = Teacher.objects.all()
    return render(request=request,template_name='crm_app/teacher.html',context={'teachers':teachers})


def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher')
        else: return redirect('add_teacher')
    form = TeacherForm
    return render(request=request,template_name='crm_app/add_teacher.html',context={'form':form})


def delete_teacher(request,id):
    if id:
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
    return redirect('teacher')

def update_teacher(request,id):
    if id and request.method == 'POST':
        teacher = Teacher.objects.get(id=id)
        form = TeacherForm(request.POST,instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher')
    else:   
        if id:
            teacher = Teacher.objects.get(id=id)
            form = TeacherForm(instance=teacher)
        else:form = TeacherForm()
    return render(request=request,template_name='crm_app/update_teacher.html',context={'form':form})

