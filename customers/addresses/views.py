'''
Created on 23/02/2012

@author: Artanit - carlosjr
'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from mitsuisushibar.customers.addresses.models import Address, AddressForm
from mitsuisushibar.customers.models import Customer, CustomerForm

    
# path /address/editar/customer_id
@login_required
def edit(request, address_id):
    address = Address.objects.get(id=address_id)
    return render_to_response('address_edit.html', locals(), context_instance=RequestContext(request))

# path /cliente/endereco/atualizar/customer_id
@login_required
def addAddress(request, customer_id):
    if request.method == 'POST':
        address = Address()
        customer = Customer.objects.get(id=customer_id)
        address.customer = customer
        form = AddressForm(request.POST, instance=address)
        if (form.is_valid()):
            address = form.save();
            customer.save()
            return redirect('/clientes')
        else:
            return render_to_response('customer_edit.html', locals(), context_instance=RequestContext(request))

def update(request, address_id):
    if request.method == 'POST':
        address = Address.objects.get(id=address_id)
        form = AddressForm(request.POST, instance=address)
        if (form.is_valid()):
            address = form.save();
            return redirect('/clientes')
        else:
            return render_to_response('address_edit.html', locals(), context_instance=RequestContext(request))
    
