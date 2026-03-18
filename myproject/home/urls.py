from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('welco/<int:age>/', views.welco, name='welco'),
    path('reg/', views.Empreg, name='empreg'),
    path('mystatic/', views.mystatic, name='mystatic'),
    path('', views.myhome, name='home'),
    path('list/', views.emp_list, name='emp_list'),
    path('del/<int:id>/', views.emp_del, name='emp_del'),
    path('edit/<int:i>/', views.emp_edit, name='emp_edit'),
    path('update/<int:i>/', views.emp_update, name='emp_update'),
    path('stud_reg/', views.stud_reg, name='stud_reg'),
    path('login/', views.user_login, name='login'),
    path('student/', views.StudentCreateView.as_view(), name='student-add'),
    path('student/list/', views.StudentListView.as_view(), name='student-list'),
    path('student/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student-delete'),
    path('student/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student-update'),
]