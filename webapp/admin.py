from django.contrib import admin
from webapp.models import User, Article, Comment, Ranking

# Register your models here.

admin.site.register(User)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Ranking)
