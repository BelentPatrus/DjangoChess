from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def index(request):

    return render(request, 'index.html')

def newIndex(request):
    rangeset = range(1, 9)
    context = {
        "range": rangeset,
    }

    return render(request, 'newIndex.html', context)


def stats(request):

    return render(request, 'stats.html')


def settings(request):

    return render(request, 'settings.html')
