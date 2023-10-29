from django.db import models

# Create your models here.

#from django.db import models
from django.contrib.auth.models import User
from user1app.models import profile
# Create your models here.
class follow_model(models.Model):
    profile_follow=models.ForeignKey(profile,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_following=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    