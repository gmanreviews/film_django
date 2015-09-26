from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django import forms

from .models import User, Person, Location
from .forms import LoginForm

# Create your views here.

def index(request):
    latest_user = User.objects.order_by('username')[:1]
    context = {'latest_user': latest_user}
    #return HttpResponse("Here are some users.")
    return render(request, 'index.html', context)

def login(request, username):
    return HttpResponse("Login Page %s."
                        % username)

def create(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = form.save(commit=0)
			if User.autheticate_user(user.username, user.password):
				return HttpResponse("YES")
			else:
				return HttpResponse("NO")
		else:
			return HttpResponse("BAD FORM")
	else:
		form = LoginForm()
		return render(request, 'create_model_form.html',{'form':form})
