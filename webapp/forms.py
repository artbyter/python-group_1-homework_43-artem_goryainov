from django import forms
from webapp.models import Article, Comment


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'author']


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['article', 'text', 'author']


class SearchArticleForm(forms.Form):
    article_name = forms.CharField(max_length=100, required=False, label="Заголовок статьи")


class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        exclude=['author','article']

