from django import forms
from django.core.exceptions import ValidationError
from .models import User, Person, Location

class UserForm(forms.ModelForm):
	username = forms.username_field{
		label = "username",
		required = True,
	}
	password = forms.password_field{
		label = "password",
		required = True,
		widget = forms.PasswordInput(),
	}

	class Meta:
		model = User

	def __init__(self, *args, **kwargs)
		return super(UserForm, self).__init__(*args, **kwargs)