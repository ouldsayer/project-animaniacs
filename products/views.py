from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from measures.models import Measure
from categories.models import Category
from models import Product, ProductForm

def load():
    categories = Category.objects.all().order_by('name')
    measures = Measure.objects.all().order_by('unit')
    return categories, measures

@login_required
def index(request):
    products = Product.objects.all().order_by('name')
    return render_to_response('products.html', locals(), context_instance=RequestContext(request))

# path /produto/nova
@login_required
def new(request):
    categories, measures = load()
    return render_to_response('product_new.html', locals(), context_instance=RequestContext(request))
    
# path /produto/editar/product_id
@login_required
def edit(request, product_id):
    categories, measures = load()
    product = Product.objects.get(id=product_id)
    return render_to_response('product_edit.html', locals(), context_instance=RequestContext(request))

# path /produto/salvar
@login_required
def create(request):
    if request.method == 'POST':
        product = Product()
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/productos')
        else:
            categories, measures = load()
            return render_to_response('product_new.html', locals(), context_instance=RequestContext(request))
            
# path /produto/atualizar/product_id
@login_required
def update(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/productos')
        else:
            categories, measures = load()
            return render_to_response('product_edit.html', locals(), context_instance=RequestContext(request))            

# path /produto/deletar/product_id
@login_required
def delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('/productos')
