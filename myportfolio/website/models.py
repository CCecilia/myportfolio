
from __future__ import unicode_literals
from django.db import models

class ProfileUser(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    title = models.CharField(max_length=200, blank=False, null=False)
    cell_phone = models.CharField(max_length=10, blank=False, null=False)
    office_phone = models.CharField(max_length=10)
    email = models.CharField(max_length=200, blank=False, null=False)
    about_me = models.TextField(blank=False, null=False)
    resume = models.FileField(upload_to='resumes/')
    facebook_profile_link = models.URLField()
    twitter_profile_link = models.URLField()
    linkedin_profile_link = models.URLField()
    github_profile_link = models.URLField()
    google_plus_profile_link = models.URLField()
    stackoverflow_profile_link = models.URLField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField()

    def __str__(self):
        return str(self.name)

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    built_with = models.ManyToManyField('ProgrammingLanguage')

    def __str__(self):
        return str(self.name)

class TutorialComment(models.Model):
    comment = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class TutorialStep(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    order_number = models.IntegerField()

    def __str__(self):
        return str(self.name)


class Tutorial(models.Model):
    SKILL_LEVELS = (
        ('1', 'Beginner'),
        ('2', 'Intermediate'),
        ('3', 'Advanced'),
    )

    name = models.CharField(max_length=200)
    language_used = models.CharField(max_length=200, blank=False, null=False)
    steps = models.ManyToManyField('TutorialStep')
    comments = models.ManyToManyField('TutorialComment')
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    git_repo_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    skill_level = models.CharField(max_length=1, choices=SKILL_LEVELS)

    def __str__(self):
        return str(self.name)