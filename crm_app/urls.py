from django.urls import path
from .views import index,student,add_student,science,teacher,add_teacher,add_science,delete_student,update_student,update_science,delete_science,update_teacher,delete_teacher
urlpatterns = [
    path('',index,name='index'),
    path('student/',student,name='student'),
    path('add_student/',add_student,name='add_student'),
    path('delete_student/<int:id>',delete_student,name='delete_student'),
    path('update_student/<int:id>/',update_student,name='update_student'),
    path('science/',science,name='science'),
    path('add_science/',add_science,name='add_science'),
    path('delete_science/<int:id>',delete_science,name='delete_science'),
    path('update_science/<int:id>/',update_science,name='update_science'),
    path('teacher/',teacher,name='teacher'),
    path('teacher/add_teacher/',add_teacher,name='add_teacher'),
    path('delete_teacher/<int:id>',delete_teacher,name='delete_teacher'),
    path('update_teacher/<int:id>/',update_teacher,name='update_teacher')
    
]