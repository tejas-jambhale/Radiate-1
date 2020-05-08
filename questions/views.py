from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import lower

from .forms import TeamForm
from .models import Question, Team, Problem
from django.urls import reverse


# Create your views here.
@login_required(login_url='users:login')
def detailView(request, pk):
    team = Team.objects.get(username=request.user.id)
    if pk == team.set_selected:
        question_list = Question.objects.filter(set_number=pk).order_by('order_number')
        team_current = team.current_question
        if team_current == 6:
            return HttpResponseRedirect(reverse('problem', args=(pk,)))
        else:
            question = question_list.get(order_number=team_current)
            context = {'question': question}
            return render(request, 'questions/question.html', context)
    else:
        return HttpResponseRedirect(reverse('nope'))


def select(request):
    try:
        team = Team.objects.get(username=request.user.id)
    except(KeyError, Team.DoesNotExist):
        if request.user.is_authenticated:
            if request.method == 'POST':
                form = TeamForm(request.POST)
                if form.is_valid():
                    name = form.cleaned_data['team_name']
                    my_set = request.POST['radio']
                    t = Team(name=name, username=request.user, set_selected=my_set)
                    t.save()
                    return HttpResponseRedirect(reverse('detail', args=(my_set,)))

            form = TeamForm()
            return render(request, 'questions/select.html', {'form': form})
        else:
            return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponseRedirect(reverse('detail', args=(team.set_selected,)))


@login_required(login_url='users:login')
def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if lower(question.answer_text) == lower(request.POST['answer']):
        team = Team.objects.get(username=request.user.id)
        team.current_question += 1
        team.score += 1
        team.save()
        return HttpResponseRedirect(reverse('success'))
    else:
        return render(request, 'questions/question.html', {
            'question': question,
            'error_message': "Your answer is incorrect",
        })


@login_required(login_url='users:login')
def success(request):
    team = Team.objects.get(username=request.user.id)
    pk = team.set_selected
    num = team.current_question
    if num == 6:
        return HttpResponseRedirect(reverse('problem', args=(pk,)))
    else:
        context = {'pk': pk, 'num': num}
        return render(request, 'questions/success.html', context)


@login_required(login_url='users:login')
def problem(request, pk):
    team = Team.objects.get(username=request.user.id)
    if pk == team.set_selected:
        problem_statement = Problem.objects.get(number=pk)
        context = {'problem': problem_statement}
        return render(request, 'questions/problem.html', context)
    else:
        return HttpResponseRedirect(reverse('nope'))


@login_required(login_url='users:login')
def nope(request):
    team = Team.objects.get(username=request.user.id)
    pk = team.set_selected
    context = {'pk': pk}
    return render(request, 'questions/nope.html', context)


@login_required(login_url='users:login')
def score(request):
    team = Team.objects.get(username=request.user.id)
    pk = team.set_selected
    num = team.score
    x = num * 20
    context = {'pk': pk, 'x': x}
    return render(request, 'questions/score.html', context)
