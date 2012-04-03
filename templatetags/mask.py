from django import template

register = template.Library()

@register.filter(name='mask')
def mask(value, pattern):
    str_value = str(value)
    if not value or len(str_value) < pattern.count('x'):
        return ''

    return pattern.replace('x', '%s') % tuple(str_value)
