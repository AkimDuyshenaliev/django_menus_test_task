from django import template
from ..views import get_context


register = template.Library()

@register.inclusion_tag('tree_menu/menu_tree.html', takes_context=True)
def draw_menu(context, name):
    return get_context(request=context.request, menuName=name)