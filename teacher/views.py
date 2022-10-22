from django.shortcuts import render

# Create your views here.
def t_home(request):
    return render(request,'teacher/t_home.html')

def prof(request):
    return render(request,'teacher/profile.html')

def view_st(request):
    return render(request,'teacher/view_student.html')

def add_st(request):
    return render(request,'teacher/add_student.html')

def chg_pwd(request):
    return render(request,'teacher/change_password.html')