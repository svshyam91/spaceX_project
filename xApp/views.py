from django.shortcuts import render
from django.http import HttpResponse
from . import spacex_api

def index(request):
    all_data = spacex_api.spaceX_api(None)
    return render(request, 'xApp/index.html', {'all_data': all_data})

def filters(request):
    all_filters = {}
    if request.method == 'GET':
        print('something')
        if 'launch_success' in request.GET:
            all_filters['launch_success'] = request.GET['launch_success']
        if 'land_success' in request.GET:
            all_filters['land_success'] = request.GET['land_success']
        if 'launch_year' in request.GET:
            all_filters['launch_year'] = request.GET['launch_year']

        all_data = spacex_api.spaceX_api(all_filters)    

    return render(request, 'xApp/filters.html', {'all_data': all_data})

