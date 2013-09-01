from django import template

register = template.Library()


@register.inclusion_tag(file_name='bootstrap_messages.html')
def bootstrap_messages(messages, icon_remove_class=None):
    """
    Render django.contrib.messages messages as bootstrap alert blocks.
    Display only info, success, error and warning level messages.

    messages - django.contrib.messages.storage.fallback.FallbackStorage instance.
    icon_remove_class - if 'None' alert will not have close button. Use bootstrap glyphs class. Example: 'icon-remove'

    Example of use:
     {% bootstrap_messages messages 'icon-remove' %}
    """

    return {'messages': messages, 'icon_remove_class': icon_remove_class}
