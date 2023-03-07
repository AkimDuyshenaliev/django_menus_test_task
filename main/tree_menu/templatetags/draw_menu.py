from django import template


register = template.Library()

@register.tag(name='draw_menu')
def get_menu(*args):
    return "Test"