from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'), 
    path('reset_password/', views.reset_password, name='reset_password'),
    path('', views.home, name='home'),  
    path('quiz/<int:category_id>/', views.quiz, name='quiz'), 
    path('submit_quiz/<int:category_id>/', views.submit_quiz, name='submit_quiz'), 
]
