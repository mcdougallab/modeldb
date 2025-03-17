from django import template

register = template.Library()

@register.filter
def get_attribute(objects, attribute):
    return [getattr(obj, attribute) for obj in objects]

@register.filter
def get_item(objects, name):
    return [obj[name] for obj in objects]