from django.urls import path
from . import views

urlpatterns = [
    path('home_page',views.home,name='hom'),
    path('admin_login',views.a_login,name='a_login'),
    path('student_login',views.s_login,name='s_login'),
    path('teacher_login',views.t_login,name='t_login')    
]