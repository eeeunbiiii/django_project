from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView): #listview 제너릭뷰 사용 (오브젝트 리스트 보여줌)
    template_name = 'polls/index.html' #원하는 템플릿 이름 임의로 지정
    context_object_name = 'latest_question_list' # 변수 이름 임의로 지정

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView): #detailview 제너릭 뷰 사용 (오브젝트 디테일 보여줌)
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        #reques.POST : 파이썬 사전과 비슷한 오브젝트 => choice오브젝트의 ID를 문자열로 리턴
        #request.POST의 값들은 항상 문자열
        #POST데이터에 choice가 없으면 KeyError발생
    except (KeyError, Choice.DoesNotExist):
        # 에러 메시지와 함께 폼을 다시 보여줌
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message' : "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1 #초이스 카운트 증가
        selected_choice.save()
        # HttpREsponseRedirect 리턴 (POST 데이터를 성공적으로 핸들링 했을때 항상 redirect)
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # reverse()함수는 우리가 보고싶은 뷰의 이름과 뷰를 가리키는 url 패턴의 변수를 받는다
    # 위 같은 경우 , /polls/3/results/를 리턴하게 됨
    