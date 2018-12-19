from django.db import models
from datetime import datetime


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    email = models.EmailField(max_length=254, verbose_name='Email')
    favorites = models.ManyToManyField('Article', blank=True, related_name='marked_by',
                                       verbose_name='Избранное')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=254, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    publish_date = models.DateTimeField(default=datetime.now, verbose_name='Дата публикации')
    author = models.ForeignKey('User', on_delete=models.PROTECT, verbose_name='Автор')
    rankings = models.ManyToManyField('User', through='Ranking', related_name='rated_by',
                                      verbose_name='Оценки')

    def __str__(self):
        return self.title


class Comment(models.Model):
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True,
                               verbose_name='Родительский комментарий')
    article = models.ForeignKey('Article', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статья')
    text = models.TextField(max_length=3000, verbose_name='Комментарий')
    author = models.ForeignKey(User, default=None, on_delete=models.PROTECT, verbose_name='Автор')


class Ranking(models.Model):
    rank = (
        (1, "Ужасно"),
        (2, "Плохо"),
        (3, "Нормально"),
        (4, "Хорошо"),
        (5, "Отлично"),
    )
    rank_dict ={key:value for key,value in rank}
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    article = models.ForeignKey('Article', on_delete=models.PROTECT)
    ranking = models.IntegerField(choices=rank, verbose_name='Оценка')
