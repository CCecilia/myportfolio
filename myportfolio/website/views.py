from django.shortcuts import render
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
