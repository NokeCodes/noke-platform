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

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    @property
    def active_members(self):
        return self.members.filter(membership__is_active=True)

    @property
    def owners(self):
        return self.members.filter(membership__is_active=True,
                                   membership__type=Membership.OWNER)

    @property
    def leaders(self):
        return self.members.filter(membership__is_active=True,
                                   membership__type__in=[Membership.OWNER, Membership.LEADER])

    @property
    def participants(self):
        return self.members.filter(membership__is_active=True,
                                   membership__type=Membership.INVOLVED)

    @property
    def prospects(self):
        return self.members.filter(membership__is_active=True,
                                   membership__type=Membership.INTERESTED)

    def __str__(self):
        return self.title


class Membership(models.Model):
    OWNER = 0
    LEADER = 1
    INVOLVED = 2
    INTERESTED = 3
    MEMBER_TYPES = (
        (OWNER, 'Owner'),
        (LEADER, 'Leader'),
        (INVOLVED, 'Involved'),
        (INTERESTED, 'Interested'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    type = models.IntegerField(choices=MEMBER_TYPES, default=INTERESTED)
    is_active = models.BooleanField(default=True)

    date_initiated = models.DateTimeField(null=True, default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    date_first_involved = models.DateTimeField(null=True)

    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return '{}<->{} ({})'.format(self.user, self.project, self.get_type_display())

    @property
    def is_leader(self):
        return self.type in (self.OWNER, self.LEADER)
