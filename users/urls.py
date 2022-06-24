from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'users'
urlpatterns = [
    path('signin', views.SignInView.as_view(), name='signin'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('logout', LogoutView.as_view(), name='logout')
]