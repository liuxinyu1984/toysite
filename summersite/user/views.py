from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .forms import MyUserCreationForm, MyUserChangeForm
from django.urls import reverse_lazy




def register(request):
    return render(request, 'registration/signup.html', {})

class SignUpView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

