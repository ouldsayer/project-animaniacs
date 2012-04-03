# -*- coding: utf-8 -*-
'''
Created on 23/02/2012

@author: Artanit - carlosjr
'''
from django.contrib.localflavor.br.forms import BRCPFField, BRCNPJField
from django.db import models
from django.db.models import Q
from django.forms import ModelForm
#TODO

class Customer(models.Model):
    name = models.CharField("Nome", max_length=200, blank=False, null=False, unique=False)
    email = models.EmailField("Email", blank="", null=True, unique=False)
    cpf = models.CharField("CPF", max_length=30, blank=True, null=True, unique=True)
       
    def __unicode__(self):
        return self.name

    @classmethod
    def split_and_search(cls, keywords):
        return cls.search(keywords.split(' '))
    
    @classmethod
    def search(cls, keywords):
        query = Q()        
        for keyword in keywords:
            '''
            if keyword.isdigit():
                query = query | Q(phone__icontains=keyword)
            else:
                query = query | Q(name__icontains=keyword) | Q(address__icontains=keyword)
            '''
            query = query | Q(name__icontains=keyword) | Q(email__icontains=keyword)
        return cls.objects.filter(query).order_by('name')    

class CustomerForm(ModelForm):
    cpf = BRCPFField(label=u'CPF')
    class Meta:
        model = Customer
