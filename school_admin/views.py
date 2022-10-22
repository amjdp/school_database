from django.shortcuts import render
from . models import Teacher

# Create your views here.
def a_home(request):
    return render(request,'school_admin/a_home.html')

def add_tr(request):
    if request.method == 'POST':
        t_name = request.POST['teacher_name']
        t_email = request.POST['teacher_email']
        t_qualification = request.POST['qualification']
        t_dob = request.POST['birthdaytime']
        t_phone = request.POST['teacher_phone']
        t_exp = request.POST['experience']
        t_photo = request.FILES['tr_photo']        
        teacher = Teacher(teacher_name = t_name, teacher_email = t_email, qualification = t_qualification, 
        teacher_dob = t_dob, teacher_phone = t_phone, exp = t_exp, teacher_profile_picture = t_photo  )
        
        teacher.save()
    return render(request,'school_admin/add_teacher.html')

def view_st(request):
    return render(request,'school_admin/view_student.html')

def view_tr(request):
    return render(request,'school_admin/view_teachers.html')

def chg_pwd(request):
    return render(request,'school_admin/change_password.html')