# encoding: utf-8
'''
Created on 20/02/2012

@author: carlosjr
'''

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User, check_password
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

#@login_required
#def main(request):
#    return render_to_response('main.html', locals(), context_instance=RequestContext(request))

def index(request):
    return render_to_response('login.html', locals(), context_instance=RequestContext(request))

def login(request):
    username=request.POST['username']
    password=request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return redirect('/categorias')
        else:
            print "Sua conta foi desabilitada!"            
            return render_to_response('login.html', locals(), context_instance=RequestContext(request))
    else:
        print "Seu username e senha estavam incorretos."  
        return render_to_response('login.html', locals(), context_instance=RequestContext(request))
        
@login_required
def logout_view(request):
    logout(request)
    return render_to_response('login.html', locals(), context_instance=RequestContext(request))
