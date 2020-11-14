from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver, Signal
from calendar_app.models import Profile
from group.models import Group, GroupMembers


@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user_name = instance)
    print(instance)


@receiver(post_save, sender = Group)
def create_groupmember(sender, instance,**kwargs):
    GroupMembers.objects.create(group = instance, member_name = instance.creator)
    print(instance)
