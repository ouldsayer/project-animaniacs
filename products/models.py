# -*- coding: utf-8 -*-

from django.db import models
from django import forms

class Product(models.Model):
    name = models.CharField("Nome", max_length=200, blank=False, null=False)
    code = models.IntegerField("Código", blank=False, null=False)
    price = models.DecimalField("Preço", blank=False, null=False, max_digits=4, decimal_places=2, default='00,00')
    tax = models.DecimalField("Contribuição", null=False, max_digits=4, decimal_places=2, default='00,00')

    has_stock = models.BooleanField("Tem Estoque", default=True)
    current_stock = models.IntegerField("Estoque Atual", default=0, null=False)
    least_stock = models.IntegerField("Estoque Mínimo", default=0, null=False)

    measure = models.ForeignKey('measures.Measure', verbose_name="Unidade de Medida", blank=False, null=False)
    category = models.ForeignKey('categories.Category', verbose_name="Categoria", blank=False, null=False)
    
    @property
    def items(self):
        return Item.objects.filter(main_product=self).order_by('main_product')

    def __unicode__(self):
        return self.name
        
        
class Item(models.Model):
    main_product = models.ForeignKey('Product', related_name="main_product", verbose_name="Produto", blank=False, null=False)
    item = models.ForeignKey('Product', related_name="item", verbose_name="Item", blank=False, null=False)
    quantity = models.IntegerField("Quantidade")

    def __unicode__(self):
        return self.main_product + " - " + self.item + " - " + self.least_stock        


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['price'].localize = True
        self.fields['price'].widget.is_localized = True
        self.fields['tax'].localize = True
        self.fields['tax'].widget.is_localized = True

    class Meta:
        model = Product
        
        
class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
