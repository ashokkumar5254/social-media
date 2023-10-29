from django import forms
from .models import Comment
class comment_form(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 4}))
    class Meta:
        model=Comment
        fields=['comment',]
 