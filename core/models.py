from django.db import models

# Create your models here.

class mapmusic(models.Model):
    musicname= models.CharField(max_length=30,null=False)
    #id = models.AutoField(primary_key=True)
    lat = models.CharField(max_length=30)
    lng = models.CharField(max_length=30)
    uploaderemail = models.EmailField()
    uploadtime = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    display = models.BooleanField(default=True,null=False)
    reviewtext = models.TextField()
    musicfile = models.FileField(upload_to='')

def __str__(self):              # __unicode__ on Python 2
    return self.musicname
