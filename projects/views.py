from django.shortcuts import render, get_object_or_404

from projects.models import Project


def index(request):
    projs = Project.objects.all()
    context = {
        'test': "Blah",
        'projs': projs,
    }
    return render(request, 'projects/index.html', context)


def details(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project': project,
    }
    return render(request, 'projects/details.html', context)