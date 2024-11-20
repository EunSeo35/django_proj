from django.contrib import admin
from blog.models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','thumbnail'] #admin 페이지 화면에 노출 

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass