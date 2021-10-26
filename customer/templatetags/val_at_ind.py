from django import template
from customer.models import *

register = template.Library()


@register.filter()
def val_at_key(dict_, key_):
    return dict_[key_]

@register.filter()
def multiply(val1, val2):
    return val1 * val2

@register.filter()
def concatenate(val1, val2):
    val1 = str(val1)
    val1 = val1.replace(' ', '_')
    return str(val1) + str(val2)

@register.filter()
def has_feedback(order):
    try:
        q = Feedback.objects.get(order_id=order)
        return True
    except Exception as e:
        return False

@register.filter()
def concatenate_zip(val1):
    path = "file:\\\D:\\codes\\python_codes\\sem 7\\nircas_adf\\media\\coupons\\"
    return path + str(val1) + '.zip'
