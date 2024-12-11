from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Course


# Kurslar ro‘yxati
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

# Kurs tafsilotlari
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'index.html', {'course': course})

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')

    return render (request,'registration/login.html')
    
