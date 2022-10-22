from django.urls import path
from . import views

app_name = 'school_admin'

urlpatterns = [
  path('admin_home_page',views.a_home,name='hom'),
  path('add_teacher',views.add_tr,name='add_tr'),
  path('view_teacher',views.view_tr,name='view_tr'),
  path('view_student',views.view_st,name='view_st'),
  path('change_password',views.chg_pwd,name='chg_pwd')
]