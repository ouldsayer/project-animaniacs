# -*- coding: utf-8 -*-

from django.db import models
from django.forms import ModelForm

class Category(models.Model):
    name = models.CharField("Nome", max_length=200, blank=False, null=False)
    code = models.IntegerField("Código", blank=False, null=False)

    def __unicode__(self):
        return self.name

class CategoryForm(ModelForm):
    class Meta:
        model = Category
