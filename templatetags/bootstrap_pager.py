# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.inclusion_tag(file_name='bootstrap_pager.html', takes_context=True)
def bootstrap_pager(context, page_object, previous_class=None, next_class=None):
    """
    Render bootstrap based pager.

    page_object - django.core.paginator.Page instance.
    previous_class - class for 'Previous' pager's link.
    next_class - class for 'Next' pager's link.

    Example of use:
     {% bootstrap_pager page_obj previous_class="previous" next_class="next" %}
    """

    absolute_uri = context.get('request').build_absolute_uri()

    return {'page_object': page_object,
            'previous_class': previous_class,
            'next_class': next_class,
            'absolute_uri': absolute_uri}
