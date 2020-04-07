from django import forms
from .models import Article

#합쳐놓은 놈
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']

# 기존 코드
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     content = forms.CharField(widget=forms.Textarea)