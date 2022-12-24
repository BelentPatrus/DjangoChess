from django.shortcuts import render


def home(request):
    rangeset = range(1, 9)
    context = {
        "range": rangeset,
    }
    return render(request, 'index.html', context)
