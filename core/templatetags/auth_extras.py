from django import template

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    """
    Check if a user belongs to a specific group.
    
    Usage in template:
    {% load auth_extras %}
    {% if user|has_group:"group_name" %}
        ...
    {% endif %}
    """
    if not user.is_authenticated:
        return False
    return user.groups.filter(name=group_name).exists()
