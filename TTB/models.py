from django.db import models

# Create your models here.

class DATA(models.Model):
    DayOfWeek = models.CharField(max_length=200)
    Lesson1 = models.CharField(max_length=200)
    Lesson2 = models.CharField(max_length=200)
    Break_1 = models.CharField(max_length=200, null=True, blank=True)
    Lesson3 = models.CharField(max_length=200)
    Lesson4 = models.CharField(max_length=200)
    Break_2 = models.CharField(max_length=200, null=True, blank=True)
    Lesson5 = models.CharField(max_length=200)
    Lesson6 = models.CharField(max_length=200)
    Lunch_B = models.CharField(max_length=200, null=True, blank=True)
    L_Skills = models.CharField(max_length=200, null=True, blank=True)
    Lesson7 = models.CharField(max_length=200)
    Lesson8 = models.CharField(max_length=200)
    Lesson9 = models.CharField(max_length=200)
    Games = models.CharField(max_length=200, null=True, blank=True)
    Class_Teacher = models.CharField(max_length=200)
    
    class Meta:
        abstract = True

class FORM1A(DATA):
    def __str__(self):
        return self.DayOfWeek
    

class FORM1B(DATA):
    def __str__(self):
        return self.DayOfWeek
    

class FORM2A(DATA):
    def __str__(self):
        return self.DayOfWeek
    

class FORM2B(DATA):
    def __str__(self):
        return self.DayOfWeek
    

class FORM3A(DATA):
    def __str__(self):
        return self.DayOfWeek
    

class FORM3B(DATA):
    def __str__(self):
        return self.DayOfWeek
    

class FORM4A(DATA):
    def __str__(self):
        return self.DayOfWeek
    

class FORM4B(DATA):
    def __str__(self):
        return self.DayOfWeek
    
