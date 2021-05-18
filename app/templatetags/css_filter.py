from django import template

register = template.Library()


@register.simple_tag()
def set_css_color(val, isFirst, isLast):
    if val and not isFirst and not isLast and float(val) < 0:
        return 'green'
    elif val and not isFirst and not isLast and 1 < float(val) < 2:
        return 'rgb(255, 181, 181)'
    elif val and not isFirst and not isLast and 2 <= float(val) < 5:
        return 'rgb(255, 90, 90)'
    elif val and not isFirst and not isLast and float(val) > 5:
        return 'rgb(255, 0, 0)'
    elif isLast:
        return 'grey'
