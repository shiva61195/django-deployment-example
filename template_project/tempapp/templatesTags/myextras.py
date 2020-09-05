from django import templates

register = template.Library()
@register.value(name='cut')
def cut(value,arg):
    """
    this cuts out all the value from the string!
    """
    return value.replace(arg,'')

# register.filter('cut', cut)
