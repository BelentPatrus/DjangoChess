from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    rangeset = range(1, 9)
    context = {
        "range": rangeset,
    }
    return render(request, 'index.html', context)


def homepage(request):

    return render(request, 'homepage.html')
