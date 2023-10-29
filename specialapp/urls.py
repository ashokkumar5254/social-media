from django.urls import path
from . import views
urlpatterns = [
    path('like/<int:id>',views.like_view,name='like'),
    path('comment/<int:id>',views.comment,name='comment')
   
    
]
