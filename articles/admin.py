from django.contrib import admin

from .models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "body",
        "author",
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
