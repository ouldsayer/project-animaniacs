from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from models import Item, ItemForm

def index(request):
    items = Item.objects.all().order_by('name')
    return render_to_response('itens.html', locals(), context_instance=RequestContext(request))
    
def edit(request, item_id):
    items = Item.objects.get(id=item_id)
    return render_to_response('item_form.html', locals(), context_instance=RequestContext(request))

def save(request, category_id):
    if request.method == 'POST':
        item = Item.objects.get(id=category_id)
        if item:
            form = ItemForm(request.POST, instance=item)
        else:
            form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/itens')
        else:
            return render_to_response('item_form.html', locals(), context_instance=RequestContext(request))

# path /categoria/deletar/category_id  
def delete(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect('/itens')
