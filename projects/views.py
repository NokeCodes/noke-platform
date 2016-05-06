from django.shortcuts import render
from django.template import loader

#from .models import Project


def index(request):

    context = {
        'test': "Blah",
    }
    return render(request, 'projects/index.html', context)


def show(request, project_id):

    context = {
        'project_id': project_id,
    }
    return render(request, 'projects/show.html', context)