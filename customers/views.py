'''
Created on 23/02/2012

@author: Artanit - carlosjr
'''
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from mitsuisushibar.customers.models import Customer, CustomerForm
from mitsuisushibar.customers.addresses.models import Address


# path /clientes
@login_required
def index(request):
    keywords = request.GET['keywords'] if request.GET.has_key('keywords') else u''
    customers = Customer.split_and_search(keywords)
    return render_to_response('customers.html', locals(), context_instance=RequestContext(request))

#path /cliente/nova
@login_required
def new(request):
    return render_to_response('customer_new.html', locals(), context_instance=RequestContext(request))
    
# path /cliente/editar/customer_id
@login_required
def edit(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    addresses = Address.objects.filter(customer=customer);
    return render_to_response('customer_edit.html', locals(), context_instance=RequestContext(request))

# path /cliente/salvar
@login_required
def create(request):
    if request.method == 'POST':
        customer = Customer()
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/clientes')
        else:
            return render_to_response('customer_new.html', locals(), context_instance=RequestContext(request))
            
# path /cliente/atualizar/customer_id
@login_required
def update(request, customer_id):
    if request.method == 'POST':
        customer = Customer.objects.get(id=customer_id)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/clientes')
        else:
            return render_to_response('customer_edit.html', locals(), context_instance=RequestContext(request))            

# path /cliente/deletar/customer_id
@login_required
def delete(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer.delete()
    return redirect('/clientes')