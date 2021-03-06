from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last 5 published questions."""
        return Question.objects.order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def add_question(request):
    question = Question()
    question.question_text = request.POST['new_question_text']
    question.pub_date = timezone.now()
    question.save()
    return HttpResponseRedirect(reverse('polls:index'))


def remove_question(request, question_id):
    question = Question.objects.get(id=question_id)
    question.delete()
    return HttpResponseRedirect(reverse('polls:index',))


def add_choice(request, question_id):
    question = Question.objects.get(id = question_id)
    choice = Choice()
    choice.choice_text = request.POST['new_choice_text']
    choice.question = question
    choice.save()
    return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))


def vote_or_remove_choice(request, question_id):
    if request.POST['choose'] == 'Vote':
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form
            return render(request, 'polls/detail.html',
                          {'question': question, 'error_message': "You didn't select a choice."})
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    else:
        question = Question.objects.get(id=question_id)
        choice_id = request.POST['choose']
        selected_choice = question.choice_set.get(id=choice_id)
        selected_choice.delete()
        return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))












