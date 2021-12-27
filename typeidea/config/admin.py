from django.contrib import admin

from config.models import Link, SideBar
from typeidea.base_admin import BaseOwnerAdmin
from typeidea.custom_site import custom_site


@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'owner', 'status', 'create_time')
    list_filter = ('status',)
    search_fields = ('title', 'owner')


@admin.register(SideBar)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'owner', 'status', 'create_time')
    list_filter = ('display_type', 'status')
    search_fields = ('title', 'owner')

