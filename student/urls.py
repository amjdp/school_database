from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
  path('home_page',views.s_home,name='hom'),
  path('profile',views.prof,name='prof'),
  path('change_password',views.chg_pwd,name='chg_pwd')
]