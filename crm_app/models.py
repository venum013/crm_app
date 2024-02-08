from django.db import models



class Teacher(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    #team = models.OneToOneField('Team',related_name='team', on_delete=models.CASCADE)
    speciality = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.first_name 

class Team(models.Model):
    time = models.TimeField(auto_now=False, auto_now_add=False)
    teacher = models.ForeignKey('Teacher',related_name='team_teacher', on_delete=models.CASCADE)
    degree = models.CharField(max_length=50)
    day_choice = [('juft','2'),('toq','1')]
    day = models.CharField(max_length=5,choices=day_choice)
    


class Science(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.OneToOneField('Teacher',related_name='science_teacher', on_delete=models.CASCADE)
    
    cost = models.IntegerField()
    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    science = models.ManyToManyField('Science', verbose_name= ("student_science"))
    
    teacher = models.ManyToManyField('Teacher', verbose_name=("student_teacher"))