from django.contrib import admin
from apps.tags.models import Tag
from core.mixins.mixin import AdminBaseMixin


@admin.register(Tag)  # noqa
class AdminTag(AdminBaseMixin):  # noqa
    """
    Tags admin
    """
    pass
