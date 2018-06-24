from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

from .forms import SignUpForm


class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect('home')
