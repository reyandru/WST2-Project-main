from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('accounts/login/', LoginView.as_view(template_name='quiz/login.html'), name='login'),
    path('', views.home, name='home'),  
    path('accounts/register/', views.register, name='register'),
    path('quiz/<int:category_id>/', views.quiz, name='quiz'),
    path('quiz/<int:category_id>/submit/', views.submit_quiz, name='submit_quiz'),
]
