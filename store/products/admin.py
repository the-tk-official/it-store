from django.contrib import admin
from .models import *

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'added_at', 'updated_at', 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'content',)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    search_fields = ('title',)

admin.site.register(Products, ProductsAdmin)
admin.site.register(Categories, CategoriesAdmin)