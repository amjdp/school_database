from django.shortcuts import render

# Create your views here.
def s_home(request):
    return render(request,'student/s_home.html')

def prof(request):
    return render(request,'student/profile.html')

def chg_pwd(request):
    return render(request,'student/change_password.html')