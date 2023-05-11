from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import register, login_view

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/', register, name='registration'),
    path('', include('django.contrib.auth.urls')),
]
