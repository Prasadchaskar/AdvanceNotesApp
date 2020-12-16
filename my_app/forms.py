from django import forms
from .models import Document,Textnotes

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class TextForm(forms.ModelForm):
    class Meta:
        model=Textnotes
        fields=('title','description','text')