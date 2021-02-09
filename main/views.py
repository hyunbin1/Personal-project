from django.shortcuts import render
from django.http import HttpResponse
# Question 모델 첨가
from .models import Question


# Create your views here.
# 21/02/09, Question 모델 데이터 작성일시 역순으로 조회하기 
def index(request):
    # 작성일시의 오름차순으로 목록 출력
    question_list = Question.objects.order_by('-create_date')
    # 'question_list' == object, 그냥 question_list == value
    context = {'question_list': question_list}
    # html에 출력하기 - render 함수는 context에 있는 Question 모델 데이터 question_list를 main/ question 파일에 적용하여 HTML 코드로 변환한다. 
    return HttpResponse(request, "main/question_list.html", context)