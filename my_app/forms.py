from django import forms
from .models import Document,Textnotes,Questions,Comment

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class TextForm(forms.ModelForm):
    class Meta:
        model=Textnotes
        fields=('title','description','text')

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Questions
        fields=('title','question')

class CommentForm(forms.ModelForm):
     class Meta:
         model=Comment
         fields=('name','comment',)