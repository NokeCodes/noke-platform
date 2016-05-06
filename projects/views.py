from django.shortcuts import render
from django.template import loader

from projects.models import Project


def index(request):
    projs = Project.objects.all()
    context = {
        'test': "Blah",
        'projs': projs,
    }
    return render(request, 'projects/index.html', context)


def show(request, project_id):
    p = Project.objects.get(id=project_id)
    context = {
        'project': p,
    }
    return render(request, 'projects/show.html', context)