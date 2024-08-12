from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout

def index(request):
    rangeset = range(1, 9)
    context = {
        "range": rangeset,
    }

    return render(request, 'index.html', context)


def stats(request):

    return render(request, 'stats.html')


def settings(request):

    return render(request, 'settings.html')