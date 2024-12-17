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


def reset_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        try:
            user = User.objects.get(username=username)
            if new_password == confirm_password:
                user.set_password(new_password)  
                user.save()
                messages.success(request, "Password successfully updated! You can now log in.")
                return redirect('login')
            else:
                messages.error(request, "Passwords do not match. Please try again.")
        except User.DoesNotExist:
            messages.error(request, "Username does not exist. Please try again.")

    return render(request, 'quiz/reset_password.html')
@login_required
def quiz(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return redirect('home')

    num_questions = int(request.GET.get('num_questions', 15))  
    questions = Question.objects.filter(category=category).order_by('?')[:num_questions]
    return render(request, 'quiz/quiz.html', {'category': category, 'questions': questions})

@login_required
def submit_quiz(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return redirect('home')

    num_questions = int(request.POST.get('num_questions', 15))  # Get number of questions selected
    questions = Question.objects.filter(category=category).order_by('?')[:num_questions]
    
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

    total_questions = len(questions)
    average = round((score / total_questions) * 100, 2) if total_questions > 0 else 0

    if 90 <= average <= 100:
        image = "quiz/congrats.png"
    elif 60 <= average <= 89:
        image = "quiz/great.png"
    elif 40 <= average <= 59:
        image = "quiz/nice.png"
    elif 15 <= average <= 39:
        image = "quiz/good.png"
    else:
        image = "quiz/study.png"

    return render(request, 'quiz/result.html', {
        'score': score,
        'total': total_questions,
        'average': average,
        'image': image,
        'wrong_answers': wrong_answers,
    })