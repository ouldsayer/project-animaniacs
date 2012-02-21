from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User


def index(request):
    users = User.objects.all().order_by('username')
    return render_to_response('users.html', locals(), context_instance=RequestContext(request))

def salvar(request, username, email, password):
    newUser = User.objects.create_user(username, email, password)
    newUser.is_staff = False
    newUser.save()
    return render_to_response('measure_form.html', locals(), context_instance=RequestContext(request))

def delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/usuarios')