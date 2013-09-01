from django import template

register = template.Library()


@register.inclusion_tag(file_name='bootstrap_form_errors.html')
def bootstrap_form_errors(form, icon_remove_class=None):
    """
    Render form's error messages as bootstrap alert blocks.

    form - django.forms.Form instance.
    icon_remove_class - if 'None' alert will not have close button. Use bootstrap glyphs class. Example: 'icon-remove'

    Example of use:
     {% bootstrap_form_errors form 'icon-remove' %}
    """

    errors_list = []
    for field in form:
        for error in field.errors:
            errors_list.append(error)

    return {'errors_list': errors_list, 'icon_remove_class': icon_remove_class}
