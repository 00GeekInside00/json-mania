from django.db import models

# Create your models here.
# users/models.py
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db import models
from hashids import Hashids


hashids = Hashids(salt='saltysalt', min_length=4)




class User(AbstractUser):

    #Fields to be added later.
    creator_id = models.CharField(max_length=30, blank=True,null=True)
@receiver(models.signals.post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        instance.creator_id = hashids.encode(len(instance.username)+instance.id)
        instance.save()



