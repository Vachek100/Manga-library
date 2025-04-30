from django.contrib import admin
from .models import Author, Manga


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'borrower')
    list_filter = ('status', 'author')
    search_fields = ('title', 'author__name')
