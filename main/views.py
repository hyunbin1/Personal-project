from django.core import paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
# Question 모델 첨가
from .models import Answer, Question
# 21/02/12 답변등록 - 입력시간 알려주기
from django.utils import timezone
from .forms import AnswerForm, QuestionForm
# 21/02/19 페이징기능
from django.core.paginator import Paginator

# Create your views here.
# 21/02/09, Question 모델 데이터 작성일시 역순으로 조회하기 
# 21/02/19 페이징 처리 추가
def index(request):
    # 21/02/19 입력파라미터
    page = request.GET.get('page', '1') # 페이지
    # 21/02/09 작성일시의 오름차순으로 목록 출력 - 조회
    question_list = Question.objects.order_by('-create_date')
    # 21/02/19 페이징처리
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    # 'question_list' == object, 그냥 question_list == value
    context = {'question_list': page_obj}
    # html에 출력하기 - render 함수는 context에 있는 Question 모델 데이터 question_list를 main/ question 파일에 적용하여 HTML 코드로 변환한다. 
    return render(request, 'main/question_list.html', context)
    
# 21/02/09, html에서 question_list 선택했을 때 detail페이지 만들어주기
# url에서 만든 question_id 값 가져오기
def detail(request, question_id):
    # get 방식을 사용하여 question 객체 가져오기 - 객체가 존재하지 않는다면 404페이지 뜨게하기
    question = get_object_or_404(Question, pk = question_id)
    context = {'question': question}
    return render(request, 'main/question_detail.html', context)


# 21/02/12 답변 등록 기능, 21/2/15 AnswerForm 추가
# html에서 answer_create 함수가 호출되면 request에는 사용자가 input에서 입력한 값이, question_id에는 answer 데이터 id가 넘어온다.
def answer_create(request, question_id):
    # 기존에 있는 질문이 있으면 나타내주고, 아니면 404 페이지를 나타낸다.
    question = get_object_or_404(Question, pk = question_id)
    # 21/02/15 등록 valid 확인
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            # commit=False == DB에 바로 저장하지 않고 타당성 확인이 될때까지 delay를 한다.
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
        return redirect('main:detail', question_id = question.id)
    else: 
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'main/question_detail.html', context)

    # 21/02/12 답변 등록 기능 -> 21/02/15 위 코드로 변경
    # 방법 1 - question 모델을 사용하여 answer 모델 저장하기
    # answer_set.create를 사용하여 Question 모델을 통해 Answer 모델 데이터를 생성한다. / request.POST.get('content')는 POST형식으로 전송된 form 데이터 항목 중 name이 content인 값을 의미한다. 
    # / Answer 모델이 Question 모델을 Foreign Key로 참조하고 있으므로 question.answer_set같은 표현을 사용할 수 있다. + 모델명(모두 소문자로 바꿔서 사용)_set은 question과 answer 모델의 종속성을 위한것으로 필수적이다. 
    # answer 모델 foreign key 괄호안에 related_name="" 속성을 사용하면 모델명_set대신 원하는 이름으로 바꿀수 있다. 
    # question.answer_set.create(content = request.POST.get('content'), create_date = timezone.now())
    
    # 방법 2: answer모델을 직접 사용하여 answer 모델 데이터 저장하기
    # question = get_object_or_404(Question, pk = question_id)
    # answer = Answer(question = question, content = request.POST.get('content'), create_date = timezone.now())
    # answer.save()
    # 치아점은 answer이라는 변수 하나를 추가해주어 save를 추가해준것. 


# 21/02/15 질문 등록하기
def question_create(request):
    # 질문 목록 화면에서 질문 등록하기 버튼을 누르면 POST 방식이기 때문에 질문 추가로 이어진다.
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('main:index')
    else:
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'main/question_form.html', context)