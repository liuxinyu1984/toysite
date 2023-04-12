from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import MyUserCreationForm, MyUserChangeForm
from django.urls import reverse_lazy

# def base(request):
#     return render(request, 'base.html', {})

# def index(request):
#     return render(request, 'index.html', {})

# def join(request):
#     return render(request, 'join.html', {})


def register(request):
    return render(request, 'registration/signup.html', {})

class SignUpView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')