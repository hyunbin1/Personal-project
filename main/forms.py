from django import forms
from main.models import Question

# 모델 폼 = 모델과 연결된 폼, 모델 폼 객체를 저장하면 연결된 모델의 데이터를 저장할 수 있다. 
class QuestionForm(forms.ModelForm):
    # 모델 폼은 Meta 클래스가 필수이고, Meta 클래스에는 모델 폼이 사용할 모델과 모델의 필드를 적어야한다.
    class Meta:
        # Question 모델에
        model = Question
        # 제목과 이에 따른 내용
        fields = ['subject', 'content']
        labels ={
            'subject': '제목',
            'content': '내용',
        }

        # form.as_p 부트스트렙 사용하는 법 - widgets 속성 사용하기
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }

        # label 속성 한글로 수정
