from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='quiz/login.html'), name='login'),
    path('accounts/register/', auth_views.PasswordChangeView.as_view(template_name='quiz/register.html'), name='register'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), 
    path('', include('quiz.urls')), 
]
