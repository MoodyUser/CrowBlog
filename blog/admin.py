from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'created_at',
    )

    search_fields = (
        'title',
        'slug',
    )


admin.site.register(Post, PostAdmin)