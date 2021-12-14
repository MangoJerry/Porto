from django.contrib import admin
from .models import *


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'price', 'subcat')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'subcat')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    # prepopulated_fields = {'slug': ('name',)}


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cat')
    list_display_links = ('name',)
    search_fields = ('name',)
    # prepopulated_fields = {'slug': ('name',)}


admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
