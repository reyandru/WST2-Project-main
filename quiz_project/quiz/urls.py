from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('quiz/<int:category_id>/', views.quiz, name='quiz'),  
    path('register/', views.register, name='register'),  
    path('submit_quiz/<int:category_id>/', views.submit_quiz, name='submit_quiz'),  
]
