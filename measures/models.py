# -*- coding: utf-8 -*-
'''
Created on 20/02/2012

@author: Artanit - carlosjr
'''
from django.db import models


class Measure(models.Model):
    description = models.CharField("Descrição", max_length=200, blank=False, null=False)
    unit = models.CharField("Unidade", max_length=20, blank=False, null=False)
    
    def __unicode__(self):
        return self.description
