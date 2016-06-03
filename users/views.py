from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect

from .forms import NewUserForm, UserForm, UserProfileForm


def index(request):
    users = User.objects.all().select_related('profile').order_by('username')
    return render(request, 'users/users_list.html', {
        'users': users,
    })


def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('users:profile', args=(request.user.get_username(),)))
    if request.method == 'POST':
        user_form = NewUserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            user = authenticate(username=user_form.cleaned_data.get('username'),
                                password=user_form.cleaned_data.get('password1'))
            login(request, user)
            return HttpResponseRedirect(reverse('users:edit_profile', args=(user.get_username(),)))
    else:
        user_form = NewUserForm()
    return render(request, 'registration/signup.html', {
        'user_form': user_form,
    })


def profile(request, username):
    try:
        profile_user = User.objects.select_related('profile').get(username=username)
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('users:index'))
    return render(request, 'users/profile.html', {
        'user': profile_user,
    })


@login_required
def edit_profile(request, username):
    if request.user.get_username() != username:
        # Can only edit your own profile.
        return HttpResponseRedirect(reverse('users:profile', args=(username,)))

    user = User.objects.select_related('profile').get(username=username)

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
