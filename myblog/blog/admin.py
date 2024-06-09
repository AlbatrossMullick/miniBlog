from django.contrib import admin
from .models import BlogPost, Comment, Blogger
from django.contrib.auth.models import User

# Register your models here.

class CommentInline(admin.TabularInline):
     model = Comment
     extra = 1

# class BloggerInline(admin.TabularInline):
#      model = Blogger
#      extra = 1

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
     list_display = ['title', 'blogger_name',  'post_date', 'short_description']
     list_filter = ['post_date', 'blogger_name']
     inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
     list_display = ['short_comment', 'comment_by', 'comment_date', 'blog_post']
     list_filter = ['comment_date', 'comment_by']


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
     list_display=['name', 'blogger_photo', 'phone']
     list_filter = ['name']