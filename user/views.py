from django.http import HttpResponse
from django.shortcuts import render

from .models import User

# Create your views here.

def index(request):
    latest_user = User.objects.order_by('username')[:1]
    context = {'latest_user': latest_user}
    #return HttpResponse("Here are some users.")
    return render(request, 'index.html', context)

def login(request, username):
    return HttpResponse("Login Page %s."
                        % username)
