__author__ = 'christian.cecilia1@gmail.com'
from django.contrib import admin
from .models import ProfileUser, Project, ProgrammingLanguage

admin.site.register(ProfileUser)
admin.site.register(Project)
admin.site.register(ProgrammingLanguage)
