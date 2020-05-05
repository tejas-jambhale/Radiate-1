from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question, Team
from django.urls import reverse


# Create your views here.
def detailView(request, pk):
    if request.user.is_authenticated:
        question_list = Question.objects.filter(set_number=pk).order_by('order_number')
        team = Team.objects.get(username=request.user.id)
        team_current = team.current_question
        question = question_list.get(order_number=team_current)
        context = {'question': question}
        return render(request, 'questions/question.html', context)
    else:
        return HttpResponseRedirect(reverse('login'))


# def select(request):
#     if request.method == 'GET':
#         form = CodeForm()
#         if form.is_valid():
#             code = form.cleaned_data['code']
#             print(code)
#         return render(request, '/detail.html', {'form': form})


def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if question.answer_text == request.POST['answer']:
        team = Team.objects.get(username=request.user.id)
        team.current_question += 1
        team.save()
        return HttpResponseRedirect(reverse('success'))
    else:
        return render(request, 'questions/question.html', {
            'question': question,
            'error_message': "Your answer is incorrect",
        })


def success(request):
    return HttpResponse("Success")
