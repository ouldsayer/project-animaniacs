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
    def split_and_search(cls, keywords, per_page = 20, page = 1):
        return cls.search(keywords.split(' '), per_page, page)
    
    @classmethod
    def search(cls, keywords, per_page = 20, page = 1):
        query = Q()
        for keyword in keywords:
            if keyword.isdigit():
                query = query | Q(code__icontains=int(keyword))
            else:
                query = query | Q(name__icontains=keyword)
        
        
        offset = (page-1)*per_page
        limit = page*per_page
        return cls.objects.filter(query).order_by('name')[offset:limit]

class CategoryForm(ModelForm):
    class Meta:
        model = Category
