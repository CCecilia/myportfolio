from django.core.files import File as django_file
from django.test import TestCase, Client
import lorem
from unittest import mock
from .models import *

class ProfileModelTests(TestCase):

	@classmethod
	def setUpTestData(cls):
		mock_resume = mock.MagicMock(spec=django_file, name='resume')
		mock_resume.name = 'resume.pdf'
		for i in range(5):
			ProfileUser.objects.create(
				name='test name%s' % i,
				title='title',
				cell_phone='(555)555-5555',
				office_phone='(555)555-5555',
				email='testuser%s@test.com' % i,
				about_me=lorem.paragraph,
				resume=mock_resume,
				facebook_profile_link='https://www.facebook.com/testuser%s' % i, 
				twitter_profile_link='https://www.twitter.com/testuser%s' % i,
				linkedin_profile_link='https://www.linkedin.com/testuser%s' % i,
				github_profile_link='https://www.github.com/testuser%s' % i,
				google_plus_profile_link='https://plus.google.com/+testuser%s' % i,
				stackoverflow_profile_link='https://stackoverflow.com/users/testuser%s' % i
			)

	def test_model_creation(self):
		all_profiles = ProfileUser.objects.all()
		self.assertEqual(len(all_profiles), 5)


class ProjectModelTests(TestCase):

	@classmethod
	def setUpTestData(cls):
		for i in range(5):
			ProgrammingLanguage.objects.create(
				name='test name%s' % i,
				image='https://www.python.org/static/opengraph-icon-200x200.png',
			)

		for i in range(5):
			new_project = Project.objects.create(
				name='Test Project %s' % i,
			    description=lorem.paragraph,
			    image='https://www.python.org/static/opengraph-icon-200x200.png'
		    )
			for language in ProgrammingLanguage.objects.all():
				new_project.built_with.add(language)

	def test_model_creation(self):
		all_projects = Project.objects.all()
		self.assertEqual(len(all_projects), 5)

	def test_languages_added_to_projects(self):
		for i in Project.objects.all():
			self.assertEqual(len(i.built_with.all()), 5)


class TutorialTests(TestCase):

	@classmethod
	def setUpTestData(cls):
		for i in range(5):
			Tutorial.objects.create(
				name='test tutorial %s' % i,
			    language_used='python',
			    git_repo_url='https://www.github.com/testuser%s' % i,
			    description=lorem.paragraph,
			    skill_level=1
			)

	def test_model_creation(self):
		all_tutorials = Tutorial.objects.all()
		self.assertEqual(len(all_tutorials), 5)


class ViewTests(TestCase):
	@classmethod
	def setUpTestData(cls):
		mock_resume = mock.MagicMock(spec=django_file, name='resume')
		mock_resume.name = 'resume.pdf'
		ProfileUser.objects.create(
			name='test name',
			title='title',
			cell_phone='(555)555-5555',
			office_phone='(555)555-5555',
			email='testuser@test.com',
			about_me=lorem.paragraph,
			resume=mock_resume,
			facebook_profile_link='https://www.facebook.com/testuser', 
			twitter_profile_link='https://www.twitter.com/testuser',
			linkedin_profile_link='https://www.linkedin.com/testuser',
			github_profile_link='https://www.github.com/testuser',
			google_plus_profile_link='https://plus.google.com/+testuser',
			stackoverflow_profile_link='https://stackoverflow.com/users/testuser',
			active=True
		)

		for i in range(5):
			Tutorial.objects.create(
				name='test tutorial %s' % i,
			    language_used='python',
			    git_repo_url='https://www.github.com/testuser%s' % i,
			    description=lorem.paragraph,
			    skill_level=1
			)

	def test_index_view(self):
		response = self.client.get('')
		# check reponse and template
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'htmlPages/index.html')

	def test_index_view(self):
		response = self.client.get('/tutorials/')
		all_tutorials = Tutorial.objects.all()
		# check reponse and template
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.context['tutorials']), len(all_tutorials))
		self.assertTemplateUsed(response, 'htmlPages/tutorials.html')


