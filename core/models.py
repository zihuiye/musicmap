from django.db import models

# Create your models here.

class mapmusic(models.Model):
    musicid = models.CharField(max_length=30,primary_key=True)
    lat = models.CharField(max_length=30)
    lng = models.CharField(max_length=30)
    uploaderemail = models.EmailField()
    uploadtime = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    display = models.BooleanField(default=False,null=False)
    reviewtext = models.TextField()
