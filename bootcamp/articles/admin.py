from django.contrib import admin
from bootcamp.articles.models import Article, ArticleComment, Tag

admin.site.register(Article) 
admin.site.register(ArticleComment)
admin.site.register(Tag)