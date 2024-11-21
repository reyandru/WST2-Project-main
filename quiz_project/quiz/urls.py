from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/<int:category_id>/', views.quiz, name='quiz'),
    path('accounts/login/', LoginView.as_view(template_name='quiz/login.html'), name='login'),  
    path('accounts/register/', views.register, name='register'),
]
