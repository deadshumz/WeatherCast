from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import SignUpForm, SignInForm
from django.views import generic
from django.contrib.auth import authenticate, login

# Create your views here.
def auth_user(request,username,password):
    user = authenticate(username=username, password=password)
    login(request, user)

# Registration View
class SignUpView(FormView):
    template_name = 'users/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


# Login View
class SignInView(generic.edit.FormView):
    template_name = 'users/signin.html'
    success_url = reverse_lazy('core:index')
    form_class = SignInForm

    def form_valid(self, form):
        auth_user(self.request, form.cleaned_data['username'], form.cleaned_data['password'])
        return redirect(self.success_url)