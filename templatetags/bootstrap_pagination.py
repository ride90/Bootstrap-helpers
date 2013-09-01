from django import template

register = template.Library()


@register.inclusion_tag(file_name='bootstrap_pagination.html', takes_context=True)
def bootstrap_pagination(context, page_object, pagination_class=None):
    """
    Render bootstrap based paginator.

    page_object - django.core.paginator.Page instance.
    pagination_class - location. Use 'right', 'centered' or None.

    Example of use:
     {% bootstrap_pagination page_obj 'right' %}
    """

    absolute_uri = context.get('request').build_absolute_uri()

    pagination_data = {'page_object': page_object, 'absolute_uri': absolute_uri}

    if pagination_class:
        pagination_data['pagination_class'] = 'pagination-{0}'.format(pagination_class)

    return pagination_data
