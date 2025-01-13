from django import template
import pprint as py_pprint

register = template.Library()

@register.filter
def getattr(obj, attr):
    return getattr(obj, attr)

@register.filter
def pprint(value):
    return py_pprint.pformat(value)