from django.shortcuts import render
from django.core.paginator import Paginator
from askme.models import *
import pdb
import math

def right_tags(request):
    context = {'tags': TAGS}
    return render(request, 'inc/base.html', context)


def index(request, page=1):
  
    questions, pages =  paginate(list(QUESTIONS), page)
    context =  {
        'page_url':'/index',
        'questions':questions,
        'questions_num':questions,
        'pages': pages,
        'current_page': page
        }
    return render(request, 'index.html', context)


def question(request, question_id, page=1):
    context = {'question': QUESTIONS[question_id], 'answers': ANSWERS}
    answers, pages =  paginate(list(ANSWERS), page)
    context =  {
        'question':QUESTIONS[question_id],
        'answers':answers,
        'page_url':'/question/' + str(question_id),
        'pages': pages,
        'current_page': page
        }
    return render(request, 'question.html', context)


def login(request):
    return render(request, 'login.html')


def ask(request):
    return render(request, 'ask.html')


def hot(request, page=1):
    questions, pages =  paginate(list(QUESTIONS), page)
    context =  {
        'page_url':'/hot',
        'questions':questions,
        'questions_num':questions,
        'pages': pages,
        'current_page': page
        }
    
    return render(request, 'hot.html', context)


def tag(request, tag_name, page=1):
    questions, pages =  paginate(list(QUESTIONS), page)
    context =  {
        'tag_name':tag_name,
        'page_url':'/tag/' + str(tag_name),
        'questions':questions,
        'questions_num':questions,
        'pages': pages,
        'current_page': page
        }
    
    return render(request, 'tag.html', context)


def sign_up(request):
    return render(request, 'signup.html')


def paginate(object_list, page, per_page=3):
    print(page)
    
    if page < 1:      
        page = 1

    if page >= len(object_list)/per_page:    
        page = math.ceil(len(object_list) / per_page)
        
    p = Paginator(object_list, per_page)
    return p.get_page(page), list(p.get_elided_page_range(page, on_each_side=1, on_ends=1))
