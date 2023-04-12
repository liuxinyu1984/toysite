from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import MyUserCreationForm, MyUserChangeForm

# def base(request):
#     return render(request, 'base.html', {})

# def index(request):
#     return render(request, 'index.html', {})

# def join(request):
#     return render(request, 'join.html', {})


def register(request):
    return render(request, 'registration/register.html', {})

class RegisterAccountView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'