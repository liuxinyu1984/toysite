from django.shortcuts import render
from user.models import MyUser



# test base.html
def base(request):
    return render(request, 'base.html', {})

# index page of website
def index(request):
    return render(request, 'index.html', {})

# sign-up and login page
def join(request):
    return render(request, 'join.html', {})

# personal homepage
def personal_home(request):
    return render(request, 'personal_home.html', { 'username': request.user.username })