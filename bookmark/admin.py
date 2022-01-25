from django.contrib import admin
from bookmark.models import *

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created_at', 'updated_at')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)