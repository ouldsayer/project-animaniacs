'''
Created on 20/02/2012

@author: mbstecnologia
'''
from django.shortcuts import render_to_response
from django.template import RequestContext


from models import Measure

def index(request):
    measures = Measure.objects.all().order_by('name')
    return render_to_response('measures.html', locals(),
                              context_instance=RequestContext(request))