from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404
from .models import Question
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template_name = 'polls/index.html'
    context = {
        'latest_question_list': latest_question_list,
    }
    '''
        forma longa de carregar um template, preencher um contexto e retornar um HttpResponse object
        
        template = loader.get_template(template_name)
        return HttpResponse(template.render(context, request))
    '''
    # usando um atalho
    return render(request, template_name, context)


def detail(request, question_id):
    ''''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    '''

    # atalho para usar get() e raise Http404 se o objeto não existir
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question},)


def results(request, question_id):
    response = "You´re looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You´re voting on question %s." % question_id)
