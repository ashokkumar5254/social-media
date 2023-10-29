from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    img=models.ImageField(default='default profile.jpg',upload_to='media')
    location=models.CharField(max_length=100,null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    def __str__(self):
        return self.location
    
class upload(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.FileField(upload_to='media',null=True)
    date_posted=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    def like_count(self):
        return self.like_set.all().count()
    def comment_count(self):
        return self.comment_set.all().count()
    def comments(self):
        return self.comment_set.all().order_by('-id')
    def latest_comment(self):
        return self.comment_set.all().last()