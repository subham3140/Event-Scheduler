from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.contrib import messages
from django.contrib.auth import authenticate
from .forms import *
from calendar_app.models import *
from calendar_app.views import *


def Signin(request):
    form = SigninForm()
    if request.method  == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "You have registered successfully!")
            return redirect('calendar_app:login')
        else:
            messages.warning(request, "Not registered please make a strong password or check the details to create the password!")
            return reverse('calendar_app/signin.html',{"form" : form})
    context = {
        'form':form
    }
    return render(request, 'calendar_app/signin.html',context)
