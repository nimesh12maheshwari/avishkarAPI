from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class EventTeam(models.Model):

    team_id = models.CharField(max_length=50, blank=False, null=False, default="")
    team_admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    team_name = models.CharField(max_length=256 ,blank=False, null=False, default="")
    team_members = models.ManyToManyField(User, related_name='members')
    pending_members = models.ManyToManyField(User, related_name='pending')


    def __str__(self):
        return self.team_id

    def add_team_member(self, user):
        self.team_members.add(user)

    def remove_team_member(self, user):
        self.team_members.remove(user)

    def add_pending_member(self, user):
        self.pending_members.add(user)

    def remove_pending_member(self, user):
        self.pending_members.remove(user)



class Event(models.Model):

    event_id = models.CharField(max_length=50, blank=False, null=False, default="")
    event_parent = models.CharField(max_length=50, blank=False, null=False, default="")
    event_name = models.CharField(max_length=255, blank=False, null=False, default="")
    team_size = models.IntegerField(default=1)
    event_icon_link = models.TextField(max_length=5000, blank=True, null=False, default="")
    event_poster_link = models.TextField(max_length=5000, blank=True, null=False, default="")

    event_description = models.TextField(blank=True, null=False, default="")
    event_coordinators = models.ManyToManyField(User)

    registered_teams = models.ManyToManyField(User, related_name='participants')

    def __str__(self):
        return self.event_id

    def get_teamsize(self):
        return self.team_size

    def add_coordinator(self, user):
        self.event_coordinators.add(user)

    def register_team(self, team):
        self.registered_teams.add(team)