from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True)
    about = models.TextField(default='', blank=True)
    github_url = models.URLField(blank=True)
    image_url = models.URLField(blank=True)

    members = models.ManyToManyField(User, through='Membership')

    def __str__(self):
        return self.title


class Membership(models.Model):
    OWNER = 0
    MEMBER = 1
    FOLLOWER = 2
    MEMBER_TYPES = (
        (OWNER, 'Owner'),
        (MEMBER, 'Member'),
        (FOLLOWER, 'Follower'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    type = models.IntegerField(choices=MEMBER_TYPES, default=FOLLOWER)

    date_requested = models.DateTimeField(null=True, default=timezone.now)
    date_joined = models.DateTimeField(null=True)