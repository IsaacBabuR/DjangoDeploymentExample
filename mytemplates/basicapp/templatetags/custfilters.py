from django import template
register = template.Library()

@register.filter
def cutout(value, arg):
    return value.replace(arg, '')

# register.filter('cutout',cutout) # this can be replace with the decorator @register.filter
