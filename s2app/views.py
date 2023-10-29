from django.shortcuts import render
from django.http import HttpResponse
from user1app.models import upload
from user1app.models import profile
from usersapp.models import follow_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    data2=profile.objects.all()
    data3=[]
    for i in data2:
        if i.user != request.user:
            data3.append(i)
    data4=data3[::-1]

    data=list(upload.objects.all())
    data.reverse()
    for i in data:
        if i.post.name.lower().endswith(('.jpg','.png','.jpeg')):
            i.file_type='image'
        elif i.post.name.lower().endswith('.mp3'):
            i.file_type='audio'
        elif i.post.name.lower().endswith('.mp4'):
            i.file_type='video'
        else:
            i.file_type='other'
    ashok1=follow_model.objects.all()
    ashok2 = ashok1.filter(user=request.user).values_list('profile_follow', flat=True)

    return render(request,'home.html',{'data':data,'data4':data4,'ashok1':ashok1,'ashok2':ashok2})

@login_required
def search_view(request):
    ashok1=None
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        ashok1=User.objects.filter(username__icontains=keyword)
        if ashok1:
            return render(request, 'user.html', {'ashok1': ashok1})
        else:
        # No users found, handle this case
            return render(request,'notmatch.html')
    else:
        return HttpResponse('you did not enter data')

