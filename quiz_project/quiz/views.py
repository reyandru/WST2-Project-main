from django.shortcuts import render, redirect
from .models import Category, Question, Choice

def home(request):
    categories = Category.objects.all()
    return render(request, 'quiz/home.html', {'categories': categories})

def quiz(request, category_id):
    category = Category.objects.get(id=category_id)
    questions = Question.objects.filter(category=category).order_by('?')[:10]
    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_answer = request.POST.get(str(question.id))
            if selected_answer == question.answer:
                score += 1
        return render(request, 'quiz/result.html', {'score': score, 'total': len(questions)})
    return render(request, 'quiz/quiz.html', {'category': category, 'questions': questions})
