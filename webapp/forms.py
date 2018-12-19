from django import forms
from webapp.models import Article


class ArticleForm(forms.ModelFormo):
    class Meta:
        model = Article
        fields = ['title', 'text', 'author']
