from django.urls import path
from student import views

urlpatterns = [
    path('shome',views.mystud),
    path('edit_profile/',views.edit_profile,name='edit_profile'),

]