'''
Created on 20/02/2012

@author: Artanit - carlosjr
'''
from django.db import models


class Measure(models.Model):
    name = models.CharField("Nome", max_length=200, blank=False, null=False)
    unit = models.CharField("Medida", max_length=20, blank=False, null=False)
    
    def __unicode__(self):
        return self.name