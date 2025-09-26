from django.contrib import admin
from .models import Post, Comment, Contact

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'likes_count')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_at')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'empresa', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('nome', 'email', 'empresa', 'mensagem')
