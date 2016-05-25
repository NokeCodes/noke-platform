from django import forms
from django.contrib.auth.models import User

from users.models import UserProfile


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'website', 'organization']
