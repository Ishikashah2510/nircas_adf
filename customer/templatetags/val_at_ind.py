from django import template

register = template.Library()


@register.filter()
def val_at_key(dict_, key_):
    return dict_[key_]

@register.filter()
def multiply(val1, val2):
    return val1 * val2
