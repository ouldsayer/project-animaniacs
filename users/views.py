from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    users = User.objects.all().order_by('username')
    return render_to_response('users.html', locals(), context_instance=RequestContext(request))

@login_required
def salvar(request, username, password):
    newUser = User.objects.create_user(username, password)
    newUser.is_staff = False
    newUser.save()
    return render_to_response('user_form.html', locals(), context_instance=RequestContext(request))

@login_required
def edit(request, user_id):
    user = User.objects.get(id=user_id)
    return render_to_response('user_form.html', locals(), context_instance=RequestContext(request))

@login_required
def delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/usuarios')