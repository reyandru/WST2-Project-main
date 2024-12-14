from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Question
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

@login_required
def home(request):
    categories = Category.objects.all()
    return render(request, 'quiz/home.html', {'categories': categories})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully! Please log in.")
            return redirect('login')
        else:
            messages.error(request, "There was an error creating your account. Please try again.")
    else:
        form = UserCreationForm()
    return render(request, 'quiz/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user) 
            return redirect('home')  
        else:
            context = {'error_message': 'Username and Password are incorrect'}
            return render(request, 'quiz/login.html', context)
    return render(request, 'quiz/login.html')

@login_required
def quiz(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return redirect('home')

    questions = Question.objects.filter(category=category).order_by('?')[:15]
    return render(request, 'quiz/quiz.html', {'category': category, 'questions': questions})

@login_required
def submit_quiz(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return redirect('home')

    questions = Question.objects.filter(category=category).order_by('?')[:15]
    score = 0
    wrong_answers = []

    for question in questions:
        selected_answer = request.POST.get(f'question_{question.id}')
        if selected_answer == question.answer:
            score += 1
        else:
            wrong_answers.append({
                "question": question.text,
                "your_answer": selected_answer,
                "correct_answer": question.answer,
            })

    return render(request, 'quiz/result.html', {
        'score': score,
        'total': len(questions),
        'wrong_answers': wrong_answers,
    })
