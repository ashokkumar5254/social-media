from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from user1app.models import profile,upload
from django.contrib.auth.models import User
from .models import follow_model
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def profile_view(request,user):
    data1=get_object_or_404(User,username=user)
    data=profile.objects.get(user=data1)
    data2=upload.objects.filter(user=data1)
    ashok1=follow_model.objects.filter(user=data1)
    ashok2=ashok1.count()
    ashok3=follow_model.objects.filter(profile_follow=data)
    ashok4=ashok3.count()
    ashok5=follow_model.objects.filter(user=request.user)
    ashok6=ashok5.values_list('profile_follow',flat=True)
         

    for i in data2:
            if i.post.name.lower().endswith(('.jpg','.png','.jpeg')):
                i.file_type = 'image'
            elif i.post.name.lower().endswith('.mp4'):
                i.file_type = 'video'
            elif i.post.name.lower().endswith(('.mp3', '.wav', '.ogg')):
                i.file_type = 'audio'
            else:
                i.file_type = 'other'
            
    a1=data2.count()
    return render(request,'usersprofile.html',{'data':data,'data2':data2,'a1':a1,'ashok2':ashok2,'ashok4':ashok4,'ashok6':ashok6})

@login_required
def ashok(request, user):
    try:
        data = get_object_or_404(User, username=user)
        data1 = get_object_or_404(profile, user=data)

        # Create a User instance for request.user
        current_user = request.user

        try:
            # Try to get the follow_model, if it exists
            data2 = follow_model.objects.get(profile_follow=data1, user=current_user)
            data2.delete()
        except follow_model.DoesNotExist:
            # If it doesn't exist, create it
            data2 = follow_model.objects.create(profile_follow=data1, user=current_user)

    except (User.DoesNotExist, profile.DoesNotExist):
        # Handle cases where the user or profile doesn't exist
        pass

    return redirect('home')

@login_required
def ashok8(request,id):
    data1 = get_object_or_404(profile, id=id)
    data2 = get_object_or_404(User,username=request.user)
    try:
        a1=follow_model.objects.get(profile_follow=data1, user=data2)
        a1.delete()
    except follow_model.DoesNotExist:
        a2=follow_model.objects.create(profile_follow=data1, user=data2)

    return redirect('usersprofile',user=data1.user)


@login_required
def followers(request,user):
    data=User.objects.get(username=user)
    data1=profile.objects.get(user=data)
    data2=follow_model.objects.filter(profile_follow=data1)
    a1=data2.count()
    return render(request,'followers.html',{'data2':data2,'data1':data1,'a1':a1})

@login_required 
def following(request,user):
    try:
        data2=User.objects.get(username=user)
        data=follow_model.objects.filter(user=data2)
        data1=data.count()
        return render(request,'following.html',{'data':data,'data1':data1,'data2':data2})
    except User.DoesNotExist:
        pass

@login_required
def follow1(request,id):
    data1 = get_object_or_404(profile, id=id)
    data2 = get_object_or_404(User,username=request.user)
    a1=follow_model.objects.get(profile_follow=data1, user=data2)
    a1.delete()
    return redirect('following',user=data2)

@login_required
def follower1(request,user):
    data1 = get_object_or_404(profile, id=request.user.profile.id)
    data2 = get_object_or_404(User,username=user)
    a1=follow_model.objects.get(profile_follow=data1, user=data2)
    a1.delete()
    return redirect('followers',user=data1.user)

@login_required
def amar(request,username):
    data1=get_object_or_404(User,username=username)
    data=profile.objects.get(user=data1)
    data2=upload.objects.filter(user=data1)
    ashok1=follow_model.objects.filter(user=data1)
    ashok2=ashok1.count()
    ashok3=follow_model.objects.filter(profile_follow=data)
    ashok4=ashok3.count()
    ashok5=follow_model.objects.filter(user=request.user)
    ashok6=ashok5.values_list('profile_follow',flat=True)
         

    for i in data2:
            if i.post.name.lower().endswith(('.jpg','.png','.jpeg')):
                i.file_type = 'image'
            elif i.post.name.lower().endswith('.mp4'):
                i.file_type = 'video'
            elif i.post.name.lower().endswith(('.mp3', '.wav', '.ogg')):
                i.file_type = 'audio'
            else:
                i.file_type = 'other'
            
    a1=data2.count()
    return render(request,'usersprofile.html',{'data':data,'data2':data2,'a1':a1,'ashok2':ashok2,'ashok4':ashok4,'ashok6':ashok6})