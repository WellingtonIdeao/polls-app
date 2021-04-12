from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
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
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question, }
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        context = {
            'question': question,
            'error_message': "You didn't select a choice.",
        }
        return render(request, 'polls/detail.html', context)
    else:
        select_choice.votes += 1
        select_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


