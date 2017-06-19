from django import template
import collections
from menus.models import Menu
register = template.Library()
import copy


def append_in_between(list, i, val):
    return list[:i+1] + [val] + list[i+1:]


@register.inclusion_tag('menus/results.html')
def draw_menu(top_menu_name):

    # Extract value from DB
    list_menus = []
    for menu in list(Menu.objects.all()):
        menu.level = -1
        list_menus.append(menu)

    # Calculate level of each menu
    temp = copy.deepcopy(list_menus)
    while True:
        if len(set(temp)) == 1:
            break
        for i, menu in enumerate(temp):
            if menu and menu.parent:
                list_menus[i].level += 1
                temp[i] = menu.parent
            else:
                temp[i] = None

    # Sort Out
    list_menus.sort(key=lambda x: x.level)

    # Filter out with top menu
    list_menus_from_top_menu = []
    top_level = 0
    for menu in list_menus:
        if menu.name == top_menu_name:
            top_level = menu.level
            menu.level = -1
            list_menus_from_top_menu.append(menu)
        else:
            if menu.parent in list_menus_from_top_menu:
                menu.level += -1 - top_level
                list_menus_from_top_menu.append(menu)

    # Child follow with parent
    parent_child_list = []
    for menu in list_menus_from_top_menu:
        if menu.parent in parent_child_list:
            p_i = parent_child_list.index(menu.parent)
            parent_child_list = append_in_between(parent_child_list, p_i, menu)
        else:
            parent_child_list.append(menu)

    prev = 0

    # Calculate the difference with previous
    for menu in parent_child_list[1:]:
        diff = menu.level - prev
        menu.diff = diff
        menu.diff_range = range(abs(diff))
        menu.level_range = range(menu.level)
        prev = menu.level

    return {'menu_list': parent_child_list[1:]}