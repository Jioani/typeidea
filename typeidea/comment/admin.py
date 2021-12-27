from django.contrib import admin

from comment.models import Comment
from typeidea.base_admin import BaseOwnerAdmin
from typeidea.custom_site import custom_site


@admin.register(Comment, site=custom_site)
class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target', 'content', 'nickname', 'website', 'email', 'status', 'create_time')
    list_filter = ('status',)
    search_fields = ('content', 'nickname', 'email')

    save_on_top = True
    actions_on_top = True

    fields = (
        ('target', 'website'),
        ('nickname', 'email'),
        'content',
        'status'
    )
