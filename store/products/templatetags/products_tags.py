from django import template
from products.models import Categories

register = template.Library()

# Декоратор
@register.simple_tag(name='get_list_categories')
def get_categories():
    return Categories.objects.all()

@register.inclusion_tag('products/list_categories.html')
def show_categories(arg1='Hello', arg2='world!'):
    categories = Categories.objects.all()
    return {'categories': categories, 'arg1': arg1, 'arg2': arg2}