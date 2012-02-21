# -*- coding: utf-8 -*-

from django.db import models
from django.forms import ModelForm


class Item(models.Model):
    name = models.CharField("Nome", max_length=200, blank=False, null=False)
    code = models.IntegerField("Código", blank=False, null=False)
    typeItem = models.CharField("Tipo", max_length=100, blank=False, null=False)
    mesureUnit = models.CharField("Unidade de Medida", max_length=100, blank=False, null=False)
    
    def __unicode__(self):
        return self.name

class ItemForm(ModelForm):
    class Meta:
        model = Item
