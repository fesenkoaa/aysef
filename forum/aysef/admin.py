from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('id', 'auth', 'theme', 'title', 'created_at', 'updated_at')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('auth', 'theme')


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'theme')
    list_display_links = ('theme',)


class SupportAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'message', 'time')
    list_display_links = ('number',)
    search_fields = ('number',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Support, SupportAdmin)
