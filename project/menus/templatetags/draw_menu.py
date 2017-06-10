from django import template
import collections
register = template.Library()


@register.inclusion_tag('menus/results.html')
def draw_menu(menu):
    menu_dict = collections.OrderedDict()
    menu.get_children(menu_dict, level=-1)
    i,prev = 0,0
    for key, value in menu_dict.items():
        # if i:
            # menu_dict[key] = value.append[prev]
        diff = value[0] - prev
        menu_dict[key] = [diff, range(abs(diff))]
        prev = value[0]
        i += 1
    print menu_dict
    return {'menu_dict': menu_dict }