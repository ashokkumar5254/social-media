from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Like
from user1app.models import upload
from .forms import comment_form
from django.contrib.auth.decorators import login_required

@login_required
def like_view(request,id):
    try:
        data=upload.objects.get(id=id)
        data1=Like.objects.get(user=request.user,post=data)
        data1.delete()
    except Like.DoesNotExist:
        data2=upload.objects.get(id=id)
        like=Like.objects.create(user=request.user,post=data2,like=1)
    return redirect('home')

@login_required
def comment(request,id):
    data=upload.objects.get(id=id)
    if data.post.name.lower().endswith(('.jpg','.png','.jpeg')):
        data.file_type = 'image'
    elif data.post.name.lower().endswith('mp4'):
        data.file_type = 'video'
    else:
        data.file_type = 'audio'
    if request.method=='POST':
        form=comment_form(request.POST)
        if form.is_valid():
            data1=form.save(commit=False)
            data1.user=request.user
            data1.post=data
            data1.save()
            return redirect('comment',id=id)


    form=comment_form()
    return render(request,'comment.html',{'data':data,'form':form})
