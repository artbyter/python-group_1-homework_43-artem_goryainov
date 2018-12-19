"""home42 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import ArticlesListView, ArticleDetailView, UsersListView, UserDetailView, FavoritesListView, \
    ArticleCreateView, ArticleUpdateView, CommentCreateView, CommentEditView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ArticlesListView.as_view(), name='articles_list'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('users/', UsersListView.as_view(), name='users_list'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('user/<int:pk>/favorites', FavoritesListView.as_view(), name='favorites_list'),
    path('article/create', ArticleCreateView.as_view(), name='create_article'),
    path('article/<int:pk>/update', ArticleUpdateView.as_view(), name='edit_article'),
    path('article/comment/create', CommentCreateView.as_view(), name='create_comment'),
    path('comment/<int:pk>/edit', CommentEditView.as_view(), name='edit_comment'),
]
