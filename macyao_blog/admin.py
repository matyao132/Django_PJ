from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'created_at',)

admin.site.register(Post,PostAdmin)