from django.contrib import admin
from .models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


# admin panel wired up to summernote to give greater functionality
# decorator added to register the class
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """

    list_display = ('title', 'slug', 'status')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)

admin.site.register(Category)
