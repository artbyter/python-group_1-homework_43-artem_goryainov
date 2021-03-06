# Generated by Django 2.1.3 on 2018-12-16 14:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('publish_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата публикации')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=3000, verbose_name='Комментарий')),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.IntegerField(choices=[(5, 'Отлично'), (2, 'Плохо'), (3, 'Нормально'), (4, 'Хорошо'), (1, 'Ужасно')], verbose_name='Оценка')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.Article')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('favorites', models.ManyToManyField(blank=True, related_name='marked_by', to='webapp.Article', verbose_name='Избранное')),
            ],
        ),
        migrations.AddField(
            model_name='ranking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='webapp.User', verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.Comment', verbose_name='Родительский комментарий'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.User', verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='article',
            name='rankings',
            field=models.ManyToManyField(related_name='rated_by', through='webapp.Ranking', to='webapp.User', verbose_name='Оценки'),
        ),
    ]
