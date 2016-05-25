from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect

from .forms import UserForm, UserProfileForm


def index(request):
    users = User.objects.all().order_by('username')
    return render(request, 'users/users_list.html', {
        'users': users,
    })


def profile(request, username):
    try:
        profile_user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('users:index'))
    return render(request, 'users/profile.html', {
        'user': profile_user,
    })


@login_required
def edit_profile(request, username):
    if request.user.username != username:
        # Can only edit your own profile.
        return HttpResponseRedirect(reverse('users:profile', args=(username,)))

    user = User.objects.get(username=username)

    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user.profile)

        if all((user_form.is_valid(), profile_form.is_valid())):
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('users:profile', args=(username,)))
    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=user.profile)

    return render(request, 'users/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
