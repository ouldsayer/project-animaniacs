'''
Created on 12/03/2012

@author: mbstecnologia
'''
from django.db import models
from django.db.models import Q
from django.forms.models import ModelForm
from mitsuisushibar.customers.models import Customer


class Address(models.Model):
    addressBasic = models.CharField("Endereco", max_length=200, blank=False, null=False, unique=False)
    district = models.CharField("Bairro", max_length=200, blank=False, null=False, unique=False)
    postalCode = models.CharField("CEP", max_length=200, blank=True, null=True, unique=False)
    city = models.CharField("Cidade", max_length=200, blank=False, null=False, unique=False)
    phone = models.IntegerField("Telefone", max_length=30, blank=False, null=False, unique=False)
    customer = models.ForeignKey(Customer, blank=True, null=False,)
    
    def __unicode__(self):
        return self.addressBasic
    '''
    @classmethod
    def split_and_search(cls, keywords):
        return cls.search(keywords.split(' '))
    
    @classmethod
    def search(cls, keywords):
        query = Q()        
        for keyword in keywords:
            if keyword.isdigit():
                query = query | Q(phone__icontains=keyword)
            else:
                query = query | Q(addressBasic__icontains=keyword) | Q(city__icontains=keyword) | Q(district__icontains=keyword)
        
        return cls.objects.filter(query).order_by('addressBasic')
    '''

    

class AddressForm(ModelForm):
    class Meta:
        model = Address
