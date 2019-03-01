from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowDashboard.as_view(template_name='user/dashboard.html'), name='dashboard'),
    path('myaction/', MyAction.as_view(), name='my-action'),
]
