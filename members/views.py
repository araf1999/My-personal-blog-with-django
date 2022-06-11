from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'members/registration.html'
    success_url = reverse_lazy('Login')