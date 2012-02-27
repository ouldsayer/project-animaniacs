# -*- coding: utf-8 -*-
'''
Created on 23/02/2012

@author: Artanit - carlosjr
'''
from django.db import models
from django.forms import ModelForm
from django.contrib.localflavor.br.forms import BRCPFField, BRCNPJField

class Customer(models.Model):
    name = models.CharField("Nome", max_length=200, blank=False, null=False, unique=False)
    phone = models.IntegerField("Telefone", max_length=30, blank=False, null=False, unique=False)
    address = models.CharField("Endereço", max_length=200, blank=False, null=False, unique=False)
    email = models.EmailField("Email", blank="", null=True, unique=False)
    cpf = models.CharField("CPF", max_length=30, blank=True, null=True, unique=True)
    
    def __unicode__(self):
        return self.name

class CustomerForm(ModelForm):
    cpf = BRCPFField(label=u'CPF') 
    class Meta:
        model = Customer
