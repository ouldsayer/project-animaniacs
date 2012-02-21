'''
Created on 20/02/2012

@author: Artanit - Carlosjr
'''
from django.shortcuts import render_to_response
from django.template import RequestContext


from models import Measure
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    measures = Measure.objects.all().order_by('name')
    return render_to_response('measures.html', locals(),
                              context_instance=RequestContext(request))