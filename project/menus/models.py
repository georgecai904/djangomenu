# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=20, unique=True, blank=False, null=False)
    url = models.CharField(max_length=200, blank=False, null=False)
    parent = models.ForeignKey('Menu', on_delete=models.CASCADE, blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super(Menu, self).__init__(*args, **kwargs)
        self.adds = {"level": -1}

    def __str__(self):
        return self.name

    def get_children(self, menu_dict, level=-1):
        if level >= 0:
            menu_dict[self] = [level]
        children = self.menu_set.all()
        if children:
            for child in children:
                child.get_children(menu_dict, level=level + 1)

    def get_url(self):
        import urlparse
        if bool(urlparse.urlparse(self.url).netloc):
            return self.url
        else:
            return "http://localhost:8000{0}".format(self.url)
