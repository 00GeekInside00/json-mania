from django.db import models
from hashids import Hashids
from jsonfield import JSONField
from accounts.models import User
hashids = Hashids(salt='saltysalt', min_length=4)



class Project(models.Model):
    name= models.CharField(max_length=255, default="Untitled", blank=False,null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE,  blank=False, null=False, related_name="project_creator")

class Storage(models.Model):
    storage_id = models.CharField(max_length=30,blank=True)
    data = JSONField( blank=True,null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                blank=False, null=False, related_name="project")
    creator=models.ForeignKey(User,on_delete=models.CASCADE,related_name="creator")
    url=models.CharField(max_length=255, default="")
    def save(self, *args, **kwargs):
        super(Storage, self).save(*args, **kwargs)
        self.storage_id = hashids.encode(self.id)
        super(Storage, self).save(*args, **kwargs)
