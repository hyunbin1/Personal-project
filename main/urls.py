from django.urls import path
# view import 하기
from . import views

# 21/02/09, 네임스페이스를 사용하여 다른 앱과 name=""이 겹쳐도 문제 발생하지 않게 하기
app_name = 'main'

urlpatterns = [
    path('', views.index, name="index"),
    # 21/02/09 Question 모델 subject 클릭 후 detail 데이터 조회하기위한 url
    # 매핑 규칙에 의해 요청되면 question_id 에 2라는 값이 저장되고 view.detail페이지가 실행된다. 
    path('<int:question_id>/', views.detail, name="detail"),
    # 21/02/12 답변 등록
    path('answer/create/<int:question_id>/', views.answer, name="answer_create"),
]