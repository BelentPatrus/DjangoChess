from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import RegisterForm, LoginForm
from django.contrib.auth import logout
import json


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/new")
    else:
        form = LoginForm()

    context = {"form": form}
    return render(request, "registration/login.html", context)


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # username = form.cleaned_data.get("username")
            # messages.success(request, f"Account created for {username}!")
            return redirect("/new")
    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, "registration/sign_up.html", context)
