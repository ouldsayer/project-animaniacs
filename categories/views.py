from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers

from models import Category, CategoryForm
from mitsuisushibar.measures.models import Measure

# path /categorias
@login_required
def index(request):
    return render_to_response('categories.html', locals(), context_instance=RequestContext(request))

# path /categorias/buscar
def search(request):
    keywords = request.GET['keywords'] if request.GET.has_key('keywords') else u''
    per_page = int(request.GET['per_page'])
    page = int(request.GET['page'])
    json = serializers.serialize("json", Category.split_and_search(keywords, per_page, page))
    import time; time.sleep(3)
    return HttpResponse(json)

# path /categoria/nova
@login_required
def new(request):
    return render_to_response('category_new.html', locals(), context_instance=RequestContext(request))
    
# path /categoria/editar/category_id
@login_required
def edit(request, category_id):
    category = Category.objects.get(id=category_id)
    return render_to_response('category_edit.html', locals(), context_instance=RequestContext(request))

# path /categora/salvar
@login_required
def create(request):
    if request.method == 'POST':
        category = Category()
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('/categorias')
        else:
            return render_to_response('category_new.html', locals(), context_instance=RequestContext(request))
            
# path /categora/atualizar/category_id
@login_required
def update(request, category_id):
    if request.method == 'POST':
        category = Category.objects.get(id=category_id)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('/categorias')
        else:
            return render_to_response('category_edit.html', locals(), context_instance=RequestContext(request))            

# path /categoria/deletar/category_id
@login_required
def delete(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('/categorias')
