from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name='profile')

    bio = models.TextField(default='', blank=True, help_text='Markdown accepted', verbose_name='About')
    website = models.URLField(default='', blank=True)
    organization = models.CharField(max_length=100, default='', blank=True)

    @property
    def display_name(self):
        return self.user.first_name or self.user.get_username()


def create_profile(sender, **kwargs):
    user = kwargs['instance']
    if kwargs['created']:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)
