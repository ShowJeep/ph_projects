from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from car.models import Car

# Create your views here.
def register(request):
    if request.method== 'POST':
        register_form= forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully!')
            return redirect('login')
    else:
        register_form= forms.RegistrationForm()
    return render(request, 'signup.html', {'form' : register_form, 'type' : 'register'})


    
class UserLoginView(LoginView):
    template_name= 'signup.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Logged IN Successfully!!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Wrong Info')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['type']= 'Login'
        return context
    
    


@login_required
def edit_profile(request):
    # profile_form = None
    if request.method== 'POST':
        profile_form= forms.ChangeUserData(request.POST, instance= request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        profile_form= forms.ChangeUserData(instance= request.user)
    return render(request, 'edit_profile.html', {'form' : profile_form})
    


def pass_change(request):
    if request.method== 'POST':
        form= PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully!')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form= PasswordChangeForm(user= request.user)
    return render(request, 'pass_change.html', {'form' : form })


def logout_view(request):
    logout(request)
    return redirect("home")

@login_required
def profile(request):
    cars = Car.objects.filter(buyers=request.user)
    return render(request, "profile.html", {"cars": cars})