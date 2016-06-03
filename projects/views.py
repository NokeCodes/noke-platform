from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from projects.models import Project, Membership


def index(request):
    projs = Project.objects.all()
    context = {
        'projs': projs,
    }
    return render(request, 'projects/index.html', context)


def details(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project': project,
    }
    if request.user.is_authenticated():
        try:
            membership = Membership.objects.get(user=request.user, project=project)
        except Membership.DoesNotExist:
            membership = None
        context['membership'] = membership
    return render(request, 'projects/details.html', context)


def join(request, slug):
    """Toggles whether user has an active membership in the project while maintaining the membership type."""
    if request.method == 'POST' and request.user.is_authenticated() and request.user.is_active:
        project = get_object_or_404(Project, slug=slug)
        action = request.POST.get('action')
        if action == 'unjoin':
            try:
                membership = Membership.objects.get(user=request.user, project=project)
                membership.is_active = False
                membership.save()
            except Membership.DoesNotExist:
                pass
        elif action == 'join':
            membership, _ = Membership.objects.update_or_create(user=request.user, project=project,
                                                                defaults={'is_active': True})

    return HttpResponseRedirect(reverse('projects:details', args=(slug,)))
