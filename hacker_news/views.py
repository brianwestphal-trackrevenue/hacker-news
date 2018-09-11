import requests
from django.shortcuts import render


def app(request):
    return render(request, "../templates/base.html", context=None)