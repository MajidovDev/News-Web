from django.contrib import admin
from .models import News, Category, Contact
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'slug', 'publish_time', 'status']
    list_filter = ['publish_time', 'status', 'category']
    prepopulated_fields = {"slug": ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Contact)