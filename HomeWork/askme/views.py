from django.shortcuts import render
# from django.http import HttpResponse
from django.core.paginator import Paginator
# from .models import QUESTIONS
# from .models import TAGS
# from .models import ANSWERS
from askme.models import *
import pdb

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

def question(request, question_id):
    context = {'question': QUESTIONS[question_id], 'answers': ANSWERS}
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

def sign_up(request):
    return render(request, 'signup.html')

def paginate(object_list, page, per_page=3):
    if page < 0 or page >= len(object_list):
        page = 1

    p = Paginator(object_list, per_page)
    return p.get_page(page), list(p.get_elided_page_range(page, on_each_side=1, on_ends=1))
