from django.shortcuts import render
from django.http import HttpResponse
from .models import QUESTIONS
from .models import TAGS
def right_tags(request):
    context = {'tags': TAGS}
    return render(request, 'inc/base.html', context)

def index(request):
    context =  {'questions':QUESTIONS}
    return render(request, 'index.html', context)

def question(request, question_id):
    context = {'question': QUESTIONS[question_id]}
    return render(request, 'question.html', context)

def login(request):
    return render(request, 'login.html')

def ask(request):
    return render(request, 'ask.html')

def hot(request):
    context = {'questions': QUESTIONS}
    return render(request, 'hot.html', context)

def tag(request, tag_name):
    # tags = {'tags': TAGS}
    context = {'questions':QUESTIONS, 'tag_name':tag_name}
    return render(request, 'tag.html', context)