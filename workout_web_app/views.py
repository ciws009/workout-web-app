from tempfile import tempdir
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import  login_required
from django.http import HttpResponseRedirect
from .models import WorkoutMenu
from .forms import NameForm


@login_required
def workout_record(request):
    return render(request, 'workout_web_app/workout_record.html', {})

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('workout_record')
    return render(request, 'workout_web_app/signup.html', {'form':form})    

def logout(request):
    logout(request)
    
def get_name(request):
    if request.method == "post":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
        else:
            form = NameForm()
    return render(request, 'name.html', {'form': form})