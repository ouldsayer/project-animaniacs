'''
Created on 20/02/2012

@author: mbstecnologia
'''
from django.shortcuts import render_to_response
from django.template import RequestContext


def main(request):
    return render_to_response('main.html', locals(), context_instance=RequestContext(request))

def login(request):
    return render_to_response('login.html', locals(), context_instance=RequestContext(request))