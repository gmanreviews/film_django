from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from .models import User, Person, Location

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
	#if request.method == 'POST'
	#process and validate data
	#else
	#render a form
    return render(request,'create.html')