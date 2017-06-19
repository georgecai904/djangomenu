from django import template
import collections
from menus.models import Menu
register = template.Library()


@register.inclusion_tag('menus/results.html')
def draw_menu(menu):
    menu_dict = collections.OrderedDict()

    menus = Menu.objects.all()
    menu_list = [[menu, -1] for menu in menus]
    test_array = list(menus)
    pos = 0

    # Define level of each menu
    while True:
        if len(set(test_array)) == 1:
            break
        for i, menu in enumerate(test_array):
            if menu and menu.parent:
                menu_list[i][1] += 1
                test_array[i] = menu.parent
            else:
                test_array[i] = None

    # Find the position of each menu
    # menu_list.sort(key=lambda x: x[1])
    # highest_level = menu_list[-1][1]
    # # for l in range(highest_level,-1,-1):
    #
    # x = [menu for menu, level in menu_list if level == highest_level]
    # x.sort(key=lambda x: x.parent)
    # print(x)
    # Calculate the diff with previous one
    prev = 0
    for i, (menu, level) in enumerate(menu_list):
        # if i:
            # menu_dict[key] = value.append[prev]
        diff = level - prev
        menu_list[i] = [menu, diff, range(abs(diff))]
        prev = level
        i += 1


    print(menu_list)

    return {'menu_list': menu_list}