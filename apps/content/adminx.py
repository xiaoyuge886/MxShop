# goods/adminx.py

import xadmin
from .models import Content, ContentInteract, ContentTag, Tag


class ContentAdmin(object):
    list_display = [ "add_time"]
    # list_filter = ["category_type", "parent_category", "name"]
    # search_fields = ['name', ]


class ContentInteractAdmin(object):
    list_display = ["add_time"]


class ContentTagAdmin(object):
    list_display = ["add_time"]


class TagAdmin(object):
    list_display = ["add_time"]


xadmin.site.register(Content, ContentAdmin)
xadmin.site.register(ContentInteract, ContentInteractAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(ContentTag, ContentTagAdmin)
