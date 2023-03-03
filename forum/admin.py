from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'team', 'tags', 'created_on')
    search_fields = ('title', 'post_content', 'team', 'tags')
    summernote_fields = ('post_content', 'excerpt')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('name', 'tags', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_comments']
    summernote_fields = ('comment')

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
