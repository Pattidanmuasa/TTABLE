from django.shortcuts import render
from .models import *

# Create your views here.

def Home(request):
    return render(request, 'Home.html')

def Homm(request):
    return render(request, 'Homm.html')



def Form1A(request):
    Lessons = FORM1A.objects.order_by('pk')[:5]
    teacher = FORM1A.objects.order_by('pk')[:1]
    return render(request, 'Stream.html', {'Lessons':Lessons, 'teacher':teacher})

def Form1B(request):
    Lessons = FORM1B.objects.order_by('pk')[:5]
    teacher = FORM1B.objects.order_by('pk')[:1]
    return render(request, 'Stream.html', {'Lessons':Lessons, 'teacher':teacher})

def Form2A(request):
    Lessons = FORM2A.objects.order_by('pk')[:5]
    teacher = FORM2A.objects.order_by('pk')[:1]
    return render(request, 'Stream.html', {'Lessons':Lessons, 'teacher':teacher})

def Form2B(request):
    Lessons = FORM2B.objects.order_by('pk')[:5]
    teacher = FORM2B.objects.order_by('pk')[:1]
    return render(request, 'Stream.html', {'Lessons':Lessons, 'teacher':teacher})

def Form3A(request):
    Lessons = FORM3A.objects.order_by('pk')[:5]
    teacher = FORM3A.objects.order_by('pk')[:1]
    return render(request, 'Stream.html', {'Lessons':Lessons, 'teacher':teacher})

def Form3B(request):
    Lessons = FORM3B.objects.order_by('pk')[:5]
    teacher = FORM3B.objects.order_by('pk')[:1]
    return render(request, 'Stream.html', {'Lessons':Lessons, 'teacher':teacher})

def Form4A(request):
    Lessons = FORM4A.objects.order_by('pk')[:5]
    teacher = FORM4A.objects.order_by('pk')[:1]
    return render(request, 'Stream.html', {'Lessons':Lessons, 'teacher':teacher})

def Form4B(request):
    Lessons = FORM4B.objects.order_by('pk')[:5]
    teacher = FORM4B.objects.order_by('pk')[:1]
    return render(request, 'Stream.html', {'Lessons':Lessons, 'teacher':teacher})
