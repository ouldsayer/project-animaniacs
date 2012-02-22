# -*- coding: utf-8 -*-

from django.db import models
from django.forms import ModelForm

class Category(models.Model):
    name = models.CharField("Nome", max_length=200, blank=False, null=False, unique=True)
    code = models.IntegerField("Código", blank=False, null=False, unique=True)

    def __unicode__(self):
        return self.name

class CategoryForm(ModelForm):
    class Meta:
        model = Category
