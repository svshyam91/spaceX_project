from django.shortcuts import render
from django.http import HttpResponse
from . import spacex_api

def index(request):
    all_data = spacex_api.spaceX_api()
    return render(request, 'xApp/index.html', {'all_data': all_data})

