from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from app.models import CustomUser
# Create your views here.
def signup_view(request):
    logout(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        email =  request.POST.get('email')
        password =  request.POST.get('password')
        confirm_password =  request.POST.get('confirm_password')
        role =  request.POST.get('role')
        # print(username, email, password, confirm_password, role)
        if password != confirm_password:
            return HttpResponse("password does not Match.")
        user = User(username= username, email=email, password=password)
        user.save()
        role = CustomUser(role = role, user= user)
        role.save()
        if user is not None:
            login(request, user)
        return redirect('home')
    return render(request, 'signup.html')


def home(request):
    return render(request, 'home.html')

def principal_view(request):
    return render(request, 'principal.html')
def teacher_view(request):
    return render(request, 'teacher.html')
def student_view(request):
    return render(request, 'student.html')