from django.contrib import admin
from blog.models import *


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_filter = ('created_by',)


class PermissionAdmin(admin.ModelAdmin):
    list_filter = ('created_by',)


class ContentAdmin(admin.ModelAdmin):
    list_filter = ('created_by',)


class MediaAdmin(admin.ModelAdmin):
    list_filter = ('created_by',)


class CommentAdmin(admin.ModelAdmin):
    list_filter = ('created_by',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Permission, PermissionAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Comment, CommentAdmin)
