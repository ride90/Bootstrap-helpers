==============
Django bootstrap helpers
==============

Django bootstrap helpers is a collection of template tags for rendering bootstrap based components.
Also app use 'django-urltags' plugin for url generation.
Twitter bootstrap framework must be connected.


bootstrap_form_errors
============

**Usage:** ``{% bootstrap_form_errors form 'icon-remove' %}``

Render form's error messages as bootstrap alert blocks.


bootstrap_messages
============

**Usage:** ``{% bootstrap_messages messages 'icon-remove' %}``

Render django.contrib.messages messages as bootstrap alert blocks.
Display only info, success, error and warning level messages.


bootstrap_pager
============

**Usage:** ``{% bootstrap_pager page_obj previous_class="previous" next_class="next" %}``

Render bootstrap based pager.


bootstrap_pagination
============

**Usage:** ``{% bootstrap_pagination page_obj 'right' %}``

Render bootstrap based pager.

