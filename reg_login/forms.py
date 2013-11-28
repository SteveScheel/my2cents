from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreateForm(UserCreationForm):

	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter a Username'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter a Password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Your Password'}))

	def __init__(self, *args, **kwargs):
		super(UserCreateForm, self).__init__(*args, **kwargs)

		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None
			self.fields[fieldname].placeholder_text = fieldname