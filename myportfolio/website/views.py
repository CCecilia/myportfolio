from django.shortcuts import render
from django.http import JsonResponse
import smtplib
from .models import *



def index(request):
	# dec vars
	projects = Project.objects.all()

	context = {
		'page': 'index',
		'projects': projects
	}

	return render(request, 'htmlPages/index.html', context)


def tutorials(request):
	# dec vars
	tutorials = Tutorial.objects.all()

	context = {
		'page': 'tutorials',
		'tutorials': tutorials
	}

	return render(request, 'htmlPages/tutorials.html', context)

def contactMeSendEmail(request):
	name = request.POST['name']
	phone = request.POST['phone']
	email = request.POST['email']
	message = request.POST['message']

	print(name, phone, email, message)
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.login("", "password")

	# import the smtplib module. It should be included in Python by default
	

	# create response
	response = {
		'status': 'success'
	}

	# send reponse JSON
	return JsonResponse(response)
