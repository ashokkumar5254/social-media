from django.urls import path
from . import views
urlpatterns = [
    path('profile/<str:user>',views.profile_view,name='usersprofile'),
    path('ashok/<str:user>',views.ashok,name='ashok'),
    path('ashok1/<int:id>',views.ashok8,name='ashok1'),
    path('followers/<str:user>',views.followers,name='followers'),
    path('following/<str:user>',views.following,name='following'),
    path('following1/<int:id>',views.follow1,name='following1'),
    path('followers1/<str:user>',views.follower1,name='followers1'),
    path('ashok2/<str:username>',views.amar,name='amar')
]