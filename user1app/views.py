from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
#from django.shortcuts import render,redirect
from .forms import userform,user_updation,profile_updation,upload_form
from .models import profile,upload
from usersapp.models import follow_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def signup(request):
    if request.method=='POST':
        data=userform(request.POST)
        if data.is_valid():
            data.save()
            return redirect('login')
    form=userform()
    return render(request,'signup.html',{'form':form})

@login_required
def log_out(request):
    if request.method=='POST':
        return redirect('logout')
    return render(request,'log_out.html')

@login_required
def Profile(request):
    try:
        data=profile.objects.get(user=request.user)
        data1=upload.objects.filter(user=request.user)
        for i in data1:
            if i.post.name.lower().endswith(('.jpg','.png','.jpeg')):
                i.file_type = 'image'
            elif i.post.name.lower().endswith('.mp4'):
                i.file_type = 'video'
            elif i.post.name.lower().endswith(('.mp3', '.wav', '.ogg')):
                i.file_type = 'audio'
            else:
                i.file_type = 'other'
        a1=data1.count()
    except profile.DoesNotExist:
        data=profile.objects.create(user=request.user)
        data1=None
        a1=0
    b1=follow_model.objects.filter(user=request.user)
    b2=b1.count()
    c1=profile.objects.get(user=request.user)
    c2=follow_model.objects.filter(profile_follow=c1)
    c3=c2.count()
    return render(request,'profile.html',{'data':data,'data1':data1,'a1':a1,'b2':b2,'c3':c3})

@login_required
def edit_profile(request):
    if request.method=='POST':
        user_form=user_updation(request.POST,instance=request.user)
        
        profile_form=profile_updation(request.POST,request.FILES,instance=request.user.profile)
        

        if user_form.is_valid() and profile_form.is_valid():
            # Check if the new username is the same as the current username
            new_username = user_form.cleaned_data.get('username')
            if new_username != request.user.username:
                # Check if the new username is already taken
                if User.objects.filter(username=new_username).exclude(id=request.user.id).exists():
                    return HttpResponse('Username is already taken.')

            user_form.save()
            profile_form.save()
            return redirect('Profile')
        else:
            return HttpResponse('this showing invalid')

    else:
        user_form=user_updation(instance=request.user)
       
        profile_form=profile_updation(instance=request.user.profile)
        
        return render(request,'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})
    

@login_required    
def upload_view(request):
    if request.method=='POST':
        data=upload_form(request.POST,request.FILES)
        if data.is_valid():
            ashok=data.save(commit=False)
            ashok.user=request.user
            ashok.save()
            return redirect('Profile')
    form=upload_form()
    return render(request,'upload.html',{"form":form})

@login_required
def upload_edit(request,id):
    data=upload.objects.get(id=id)
    if data.post.name.lower().endswith(('.jpg','.png','.jpeg')):
        data.file_type = 'image'
    elif data.post.name.lower().endswith('.mp4'):
        data.file_type = 'video'
    elif data.post.name.lower().endswith(('.mp3', '.wav', '.ogg')):
        data.file_type = 'audio'
    else:
        data.file_type = 'other'
    return render(request,'upload_edit.html',{'data':data})


def ashok(request,user):
    print(user)
    print(type(user))
    
    return HttpResponse('this is working')
@login_required
def upload_delete(request,id):
    data=upload.objects.get(id=id)
    data.delete()
    return redirect('Profile')

    

