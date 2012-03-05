# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import Q
from django.forms import ModelForm

class Product(models.Model):
    name = models.CharField("Nome", max_length=200, blank=False, null=False)
    code = models.IntegerField("Código", blank=False, null=False)
    price = models.IntegerField("Preço", blank=False, null=False)
    tax = models.DecimalField("Contribuição", blank=False, null=False, max_digits=4, decimal_places=2, default=00.00)

    has_stock = models.BooleanField("Tem Estoque", default=True)
    current_stock = models.IntegerField("Estoque Atual")
    least_stock = models.IntegerField("Estoque Mínimo")

    measure = models.ForeignKey('measures.Measure', verbose_name="Unidade de Medida", blank=False, null=False)
    category = models.ForeignKey('categories.Category', verbose_name="Categoria", blank=False, null=False)

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

class ProductForm(ModelForm):
    class Meta:
        model = Product
