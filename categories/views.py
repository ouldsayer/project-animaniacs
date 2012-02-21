from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from models import Category, CategoryForm

# path /categorias
@login_required(redirect_field_name='/login')
def index(request):
    categories = Category.objects.all().order_by('name')
    return render_to_response('categories.html', locals(), context_instance=RequestContext(request))
    
@login_required
def edit(request, category_id):
    category = Category.objects.get(id=category_id)
    return render_to_response('category_form.html', locals(), context_instance=RequestContext(request))

@login_required
def save(request, category_id):
    if request.method == 'POST':
        category = Category.objects.get(id=category_id)
        if category:
            form = CategoryForm(request.POST, instance=category)
        else:
            form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/categorias')
        else:
            return render_to_response('form.html', locals(), context_instance=RequestContext(request))

# path /categoria/deletar/category_id
@login_required  
def delete(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('/categorias')
