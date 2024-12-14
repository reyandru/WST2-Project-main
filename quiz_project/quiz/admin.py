from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category, Question, Choice  

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Choice)

