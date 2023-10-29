from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile,upload
class userform(UserCreationForm):
    email=forms.EmailField(help_text='')
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set help_text to empty string for the password fields
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
class user_updation(forms.ModelForm):
    username=forms.CharField(help_text='')
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']
class profile_updation(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}),required=False)
    location=forms.CharField(max_length=100,required=False)
    class Meta:
        model=profile
        fields=['img','location','bio']

class upload_form(forms.ModelForm):
    class Meta:
        model=upload
        fields=['post',]
