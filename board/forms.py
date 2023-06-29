from django import forms
from board.models import Question, Answer, Review


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject' : '제목',
            'content' : '내용'
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변 내용'
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']
        labels = {
            'content': '리뷰'

        }