from django.urls import path
from django.contrib.auth import views as authviews
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('login/', views.LoginInterfaceView.as_view(), name='login'), 
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', views.LogoutInterfaceView.as_view(), name='logout'),
    path('reset_password/', authviews.PasswordResetView.as_view(template_name="home/reset_password.html"), name='reset_password'),
    path('reset_password_sent/', authviews.PasswordResetDoneView.as_view(template_name = "home/password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', authviews.PasswordResetConfirmView.as_view(template_name = "home/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', authviews.PasswordResetCompleteView.as_view(template_name = "home/password_reset_done.html"), name='password_reset_complete'),

]
