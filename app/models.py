from django.contrib.auth.models import User
from django.db import models
class CustomUser(models.Model):
	ROLE_CHOICES = (
		('teacher', 'Teacher'),
		('student', 'Student'),
		('principal', 'Principal'),
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	
	role = models.CharField(max_length=10, choices=ROLE_CHOICES)

	
