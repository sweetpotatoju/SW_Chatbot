from django import forms
from .models import Notice, QATable
from main.models import Question  # main 앱의 Question 모델을 import

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'content']


class QATableForm(forms.ModelForm):
    class Meta:
        model = QATable
        fields = ['q', 'a']

    def __init__(self, *args, **kwargs):
        super(QATableForm, self).__init__(*args, **kwargs)

        # Question 모델에서 question_content가 'N'인 것만 필터링
        unused_questions = Question.objects.filter(answer_status='N')

        # Question 필드를 새로운 QuerySet으로 업데이트
        self.fields['q'].queryset = unused_questions

