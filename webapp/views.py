from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, View, RedirectView
from webapp.models import User, Article, Ranking, Comment


# Create your views here.


class ArticlesListView(ListView):
    model = Article
    template_name = 'index.html'


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
