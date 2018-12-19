from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from webapp.models import User, Article, Comment
from webapp.forms import ArticleCreateForm, CommentCreateForm, SearchArticleForm, CommentEditForm
from django.urls import reverse_lazy


# Create your views here.


class ArticlesListView(ListView, FormView):
    model = Article
    template_name = 'index.html'
    form_class = SearchArticleForm

    def get_queryset(self):
        article_name = self.request.GET.get('article_name')
        if not article_name:
            return Article.objects.all()
        else:
            return Article.objects.filter(title__icontains=article_name)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'


class UsersListView(ListView):
    model = User
    template_name = 'users.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user.html'


class FavoritesListView(ListView):
    template_name = 'favorites.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        self.user = get_object_or_404(User, pk=self.kwargs['pk'])
        context['user'] = self.user
        return context

    def get_queryset(self):
        self.user = get_object_or_404(User, pk=self.kwargs['pk'])
        return Article.objects.filter(marked_by=self.kwargs['pk'])


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'create_article.html'
    success_url = reverse_lazy('articles_list')


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'edit_article.html'
    success_url = reverse_lazy('articles_list')


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = 'create_comment.html'
    success_url = reverse_lazy('articles_list')


class CommentEditView(UpdateView):
    model = Comment
    form_class = CommentEditForm
    template_name = 'edit_comment.html'
    success_url = reverse_lazy('articles_list')
