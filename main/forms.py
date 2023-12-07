from .models import Question
from django import forms


class RegisterQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['password', 'question_text']
