from django.shortcuts import render
from .models import Question
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def userpage(request):
    if request.method == 'POST':
        question_text = request.POST['question_text']
        password = request.POST['password']
        question = Question(question_text=question_text, password=password)
        question.save()
    return render(request, 'userpage/userpage.html', {})

@csrf_exempt
def question_form(request):
    if request.method == 'POST':
        question_text = request.POST['question']
        password = request.POST['password']
        question = Question(question_text=question_text, password=password)
        question.save()
    return render(request, 'userpage/userpage.html')