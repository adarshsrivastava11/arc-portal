from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout

from django.shortcuts import redirect
from django.contrib.auth.decorators import *
import os
from random import randint
from datetime import datetime
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


def email(to,subject,body):
    body = body + "\n\n -------------------------------------\n\n"+" This is an Auto Generated Email. Please do not reply."
    # print body
    send_mail(subject,body,'"ARC Portal" <noreply@arc-portal.com>',[to],
                          fail_silently=False)

def index(request):
	return render(request, 'index.html')

@csrf_exempt
def signup(request):
	if isinstance(request.body, bytes):
		data = json.loads(request.body.decode(encoding='utf-8'))
	else:
		data = json.loads(request.body)
	username = data['username']
	rollnumber = data['rollno']
	random_num = str(randint(1,9))+str(randint(10,99))+str(randint(1,9))
	password = random_num
	error = "None"
	if rollnumber != False:
		rollnumber = str(rollnumber)
		if User.objects.filter(username=username).exists():
			error = "User already exists"
		else:
			email_user = rollnumber+'@iitk.ac.in'
			user = User.objects.create_user(username=username,password=password,email=email_user)
			user.save()
			return JsonResponse({ 'username': username, 'rollnumber': rollnumber, 'password': password })

	return JsonResponse({ 'error': error }, status=500)
