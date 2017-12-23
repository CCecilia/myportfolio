from website.models import ProfileUser, ProgrammingLanguage


def addDefaultTemplateInformation(context):
	# get active profile & languages
	active_profiles_check = ProfileUser.objects.filter(active=True)
	languages = ProgrammingLanguage.objects.all()
	
	#create default if none
	if not active_profiles_check:
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
		active_profiles = ProfileUser.objects.filter(active=True)
	else:
		active_profiles = active_profiles_check


	# add to template
	context = {
		'activeProfile': active_profiles[0],
		'languages': languages
	}
	
	# return context with defaults
	return context