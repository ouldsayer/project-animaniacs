from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from mitsuisushibar.measures.models import Measure
from mitsuisushibar.categories.models import Category
from models import Product, ProductForm, Item, ItemForm

def load():
    categories = Category.objects.all().order_by('name')
    measures = Measure.objects.all().order_by('unit')
    products = Product.objects.all().order_by('name')
    return categories, measures, products

@login_required
def index(request):
    keywords = request.GET['keywords'] if request.GET.has_key('keywords') else u''
    products = Product.split_and_search(keywords)
    return render_to_response('products.html', locals(), context_instance=RequestContext(request))

# path /produto/nova
@login_required
def new(request):
    categories, measures = load()
    return render_to_response('product_new.html', locals(), context_instance=RequestContext(request))
    
# path /produto/editar/product_id
@login_required
def edit(request, product_id):
    categories, measures, products = load()
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
            return redirect('/produtos')
        else:
            categories, measures, products = load()
            return render_to_response('product_new.html', locals(), context_instance=RequestContext(request))
            
# path /produto/atualizar/product_id
@login_required
def update(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/produtos')
        else:
            categories, measures, products = load()
            return render_to_response('product_edit.html', locals(), context_instance=RequestContext(request))            

# path /produto/deletar/product_id
@login_required
def delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('/produtos')

# path /produto/product_id/item/deletar/item_id
@login_required
def delete_item(request, product_id, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect('/produto/editar/' + product_id)
    
# path /produto/product_id/item/salvar
@login_required
def salvar_item(request, product_id):
    if request.method == 'POST':
        form = ItemForm(request.POST)
#        import pdb; pdb.set_trace()
        if form.is_valid():
            form.save()
        return redirect('/produto/editar/' + product_id)