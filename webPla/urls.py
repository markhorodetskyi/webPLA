from django.contrib import admin
from django.urls import path, include
from user import views as userViews

from django.contrib.auth import views as authViews

urlpatterns = [
    path('', authViews.LoginView.as_view(template_name='user/login.html'), name='auth'),
    path('profile/', userViews.profile, name='profile'),
    path('exit/', authViews.LogoutView.as_view(template_name='user/exit.html'), name='exit'),
    path('admin/', admin.site.urls, name='admin'),
    path('dashboard/', userViews.ShowDashboard.as_view(template_name='user/dashboard.html'), name='dashboard'),
    path('forms/', userViews.ShowDashboard._form_view, name='user'),
    # path('dashboardC/', userViews.ShowDashboardC.as_view(template_name='user/dashboard.html'), name='dashboardC'),

    path('enter/', userViews.my_redirect, name='my_redirect'),

]
