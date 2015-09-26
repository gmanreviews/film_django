from django import forms
from django.core.exceptions import ValidationError
from .models import User, Person, Location

class LoginForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username','password')

	def __init__(self, *args, **kwargs):
		return super(LoginForm, self).__init__(*args, **kwargs)

class CreateForm(forms.ModelForm):

	class Meta:
		model = User
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		return super(CreateForm, self).__init__(*args, **kwargs)
