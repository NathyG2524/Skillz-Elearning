from django.contrib.auth.models import User
from .models import Profile


from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


def createProfile(sender, instance, created, **kwags):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            email=user.email,
            name=user.first_name,
        )

def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.email = profile.email
        user.save()


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print('Deleting User ....')

post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
# post_delete.connect(createProfile, sender=Profile)