# templatetags/custom_tags.py
from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key, '')  # Return empty string if key doesn't exist