from django.contrib import admin
from .models import Post, Category
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'body')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)