from django.db import models
from django.contrib.auth.models import User
from user1app.models import upload

class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(upload,on_delete=models.CASCADE)
    like=models.IntegerField()
    def __str__(self):
        return self.user.username
    
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    post=models.ForeignKey(upload,on_delete=models.CASCADE,null=True)
    comment=models.TextField(null=True)
    def __str__(self):
        return self.comment