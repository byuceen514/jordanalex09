from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'trailanalyzer/home.html', context)
def map(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'trailanalyzer/map.html', context)

def Video(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'trailanalyzer/Video.html', context)

def Help(request):
    """
    Controller for the app home page.
    """
    context = {}
    return render(request, 'trailanalyzer/Help.html', context)

def techdoc(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'trailanalyzer/techdoc.html', context)