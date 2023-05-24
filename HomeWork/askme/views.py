from django.shortcuts import render

from askme.models import *
import pdb
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import auth
from askme.forms import * 
from django.shortcuts import redirect
from django.urls import reverse

def right_tags(request):
    context = {'tags': TAGS}
    return render(request, 'inc/base.html', context)

# @login_required(login_url='login/')
def index(request, page=1):
    questions_, pages =  paginate(list(questions.new_q.all()), page)
    context =  {
        'page_url':'/index',
        'questions':questions_,
        'pages': pages,
        'current_page': page
        }   
    return render(request, 'index.html', context)


def question(request, question_id, page=1):
    
    try:
        question_ = questions.new_q.get(id = question_id)
    except questions.DoesNotExist:
        raise Http404("Question does not exist")

    answers_, pages =  paginate(list(answers.objects.filter(question=question_id)), page)
    context =  {
        'question':question_,
        'answers':answers_,
        'page_url':'/question/' + str(question_id),
        'pages': pages,
        'current_page': page
        }
    return render(request, 'question.html', context)

# def answer(request):
#     if request.method == 'GET':
#         print(request.GET)
#     elif request.method == 'POST':    
#         answer_form = AnswerForm(request.POST)
#         if answer_form.is_valid():
            
#     return render(request, 'question.html', context={'form':answer_form})

def log_in(request):
    
    
    if request.method == 'GET':
        login_form = LoginForm()
        
        print(request.GET)
    elif request.method == 'POST':    
        login_form = LoginForm(request.POST)
        
        print(request.POST['continue_'])
        if login_form.is_valid():
            user = auth.authenticate(request=request, **login_form.cleaned_data)
            if user:
                print("Hello")
                login(request, user)
                return redirect(reverse(request.POST['continue_']))
            login_form.add_error(None, "Invalid username or password")
    return render(request, 'login.html', context={'form':login_form})

@login_required
def ask(request):
    if request.method == 'GET':
        ask_form = AskForm()
    elif request.method == 'POST':
        ask_form = AskForm(request.POST)
        if ask_form.is_valid():
            new_q(request.POST, request.user)
            return redirect(reverse('index'))
    return render(request, 'ask.html', context={'form':ask_form})


def hot(request, page=1):
    questions_, pages =  paginate(list(questions.hot.all()), page)
    context =  {
        'page_url':'/hot',
        'questions':questions_,
        'pages': pages,
        'current_page': page
        }
    
    return render(request, 'hot.html', context)


def tag(request, tag_name, page=1):
    try:
        tag = tags.objects.get(name = tag_name)
    except tags.DoesNotExist:
        raise Http404("Tag does not exist")
    
    questions_, pages =  paginate(list(questions.new_q.filter(tags__id=tag.pk)), page)
    context =  {
        'tag_name':tag.name,
        'page_url':'/tag/' + '%23' + tag_name[1:],
        'questions':questions_,
        'pages': pages,
        'current_page': page
        }
    
    return render(request, 'tag.html', context)


def sign_up(request):
    if request.method == "GET":
        register_form = RegistrationForm()
    elif request.method == "POST":
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            us = new_us(request.POST)
            us_data = {'username': us.username, 'password': request.POST['password']}
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                user =  auth.authenticate(request=request, **login_form.cleaned_data)
                if user:
                    login(request, user)
                    return redirect(reverse('index'))
                
    return render(request, 'signup.html', context={'form':register_form})


def logout_ref(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))