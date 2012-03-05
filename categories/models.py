# -*- coding: utf-8 -*-

from django.db import models
from django.forms import ModelForm
from django.db.models import Q

class Category(models.Model):
    name = models.CharField("Nome", max_length=200, blank=False, null=False, unique=True)
    code = models.IntegerField("Código", blank=False, null=False, unique=True)

    def __unicode__(self):
        return self.name
    
    @classmethod
    def split_and_search(cls, keywords):
        return cls.search(keywords.split(' '))
    
    @classmethod
    def search(cls, keywords):
        query = Q()        
        for keyword in keywords:
            if keyword.isdigit():
                query = query | Q(code__icontains=keyword)
            else:
                query = query | Q(name__icontains=keyword)
        
        return cls.objects.filter(query).order_by('name')

class CategoryForm(ModelForm):
    class Meta:
        model = Category
