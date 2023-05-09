from django.shortcuts import render

from askme.models import *
import pdb
from django.http import Http404


def right_tags(request):
    context = {'tags': TAGS}
    return render(request, 'inc/base.html', context)


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


def login(request):
    return render(request, 'login.html')


def ask(request):
    return render(request, 'ask.html')


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
    return render(request, 'signup.html')


