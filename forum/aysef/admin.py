from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('id', 'auth', 'category', 'title', 'created_at', 'updated_at')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('auth', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    list_display_links = ('category',)


class SupportAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'message', 'time')
    search_fields = ('number',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Support, SupportAdmin)
