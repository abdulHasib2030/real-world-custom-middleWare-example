from typing import Any
from django.shortcuts import redirect, render, HttpResponse
from app.views import CustomUser



class CustomMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    
    def __call__(self,request, *args: Any, **kwds: Any) -> Any:
        print("befor view", request.user.username)
        resonse = self.get_response(request)
        if request.user.is_authenticated:
            role = CustomUser.objects.get(user = request.user.id)
            if role.role == 'principal' and request.path != '/principal/':
                return redirect('/principal/')
            elif role.role == 'teacher' and request.path != '/teacher/':
                return redirect('/teacher/')
            elif role.role == 'student' and request.path != '/student/':
                return redirect('/student/')
        
        return resonse