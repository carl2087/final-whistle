from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'team', 'tags', 'created_on')
    search_fields = ('title', 'post_content', 'team', 'tags')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'tags', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'comment')
    actions = ['approve_comments']
    summernote_fields = ('comment')

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
