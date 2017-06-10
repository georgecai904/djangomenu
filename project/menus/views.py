# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Menu


# Create your views here.


def show_menus(request):
    main_menu = Menu.objects.get(parent=None)
    return render(request, "menus/menu_list.html", {'main_menu': main_menu})


def show_menu(request, menu_id):
    main_menu = Menu.objects.get(parent=None)
    return render(request, "menus/menu_list.html", {'main_menu': main_menu, 'menu': Menu.objects.get(id=menu_id)})
