from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=LearnerProfile)
def create_learner_profile(sender, instance, created, **kwargs):
    if created:
       User.objects.create(username=instance)
@receiver(post_save, sender=LearnerProfile)
def save_learner_profile(sender, instance, **kwargs):
    instance.learnerusr.save()

@receiver(post_save, sender=CreatorProfile)
def create_creator_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(username=instance)

@receiver(post_save, sender=CreatorProfile)
def save_creator_profile(sender, instance, **kwargs):
    instance.creatorusr.save()