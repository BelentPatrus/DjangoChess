from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def index(request):

    return render(request, 'index.html')


def stats(request):

    return render(request, 'stats.html')


def settings(request):

    return render(request, 'settings.html')
