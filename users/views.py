from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# path /usuarios
@login_required
def index(request):
    keywords = request.GET['keywords'] if request.GET.has_key('keywords') else u''
    keywords.split(' ')        
    query = Q()        
    for keyword in keywords:
            query = query | Q(username__icontains=keyword) | Q(email__icontains=keyword)     
    users = User.objects.filter(query).order_by('username')
    return render_to_response('users.html', locals(), context_instance=RequestContext(request))

# path /categoria/nova
@login_required
def new(request):
    return render_to_response('user_new.html', locals(), context_instance=RequestContext(request))
    
# path /categoria/editar/user_id
@login_required
def edit(request, user_id):
    editableUser = User.objects.get(id=user_id)
    return render_to_response('user_edit.html', locals(), context_instance=RequestContext(request))

# path /categora/salvar
@login_required
def create(request):
    if request.method == 'POST':       
        passwordConfirm = request.POST['passwordConfirm']
        if request.POST['username'] and request.POST['email'] and request.POST['password'] == passwordConfirm:
            user = User.objects.create_user(request.POST['username'], request.POST['password'])
            user.email = request.POST['email']
            user.is_staff = False
            user.save()
            return redirect('/usuarios')
        else:
            mostrar = "Passwords precisam ser identicos e todos os campos preenchidos!"
            return render_to_response('user_new.html', locals(), context_instance=RequestContext(request))
            
# path /categora/atualizar/user_id
@login_required
def update(request, user_id):
    if request.method == 'POST':
        password = request.POST['password']
        passwordConfirm = request.POST['passwordConfirm']
        userUp = User.objects.get(id=user_id)
        userUp.username = request.POST['username']
        userUp.email = request.POST['email']
        if userUp.username and userUp.email and request.POST['password'] == passwordConfirm:
            if password:
                userUp.set_password(password)        
            userUp.save()
            return redirect('/usuarios')
        else:
            mostrar = "Passwords precisam ser identicos e todos os campos preenchidos!"
            editableUser = User.objects.get(id=user_id)
            return render_to_response('user_edit.html', locals(), context_instance=RequestContext(request))            

# path /deletar/user_id
@login_required
def delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/usuarios')