
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login/',auth_view.LoginView.as_view(template_name='login.html'),name='login'),
    path('log_out',views.log_out,name='log_out'),
    path('logput/',auth_view.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('Profile',views.Profile,name='Profile'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('upload',views.upload_view,name='upload'),
    path('upload_edit/<int:id>',views.upload_edit,name='upload_edit'),
    path('upload_delete/<int:id>',views.upload_delete,name='upload_delete'),
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='password_reset.html',html_email_template_name='password_reset_email.html'),name='password_reset'),
    path('password_reset_done',auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset_complete',auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
   

]
