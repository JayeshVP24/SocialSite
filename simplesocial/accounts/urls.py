from django.urls import path
from django.contrib.auth import views as aviews
from . import views

app_name = "accouts"

urlpatterns = [
    path('login/',aviews.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',aviews.LogoutView.as_view(),name='logout'),
    path('signup/',views.SignUp.as_view(),name='signup'),
]