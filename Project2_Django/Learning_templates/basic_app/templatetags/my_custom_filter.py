from django import template

register = template.Library()


#@register.filter(name='cut')
def cut(value, arg):
    """
    This will replace the args to 'developer' in value string

    """
    return value.replace(arg, 'Developer')


register.filter('cut', cut)


#@register.filter(name='first_char_upper')
def first_char_upper(value):
    '''
    This will change the 1st char to upper case in each word
    '''
    return value.capitalize()


register.filter('change', first_char_upper)


if __name__ == '__main__':
    print(first_char_upper('priyanka priyadarshini'))



