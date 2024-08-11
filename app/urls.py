from django.urls import path
from app.views import *

urlpatterns = [
    path('', signup_view, name='signup'),
    path('home/', home, name='home'),
    path('principal/', principal_view , name='principal'),
    path('teacher/', teacher_view, name='teacher'),
    path('student/', student_view, name='student'),
]