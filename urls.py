# encoding: utf-8
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mitsuisushibar.views.home', name='home'),
    # url(r'^mitsuisushibar/', include('mitsuisushibar.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    
    (r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
        
    (r'^accounts/login/$', 'mitsuisushibar.views.index'),
    (r'^login/$', 'mitsuisushibar.views.login'),
    (r'^logout/$', 'mitsuisushibar.views.logout_view'),

    (r'^categorias/$', 'mitsuisushibar.categories.views.index'),
    (r'^categoria/nova/$', 'mitsuisushibar.categories.views.new'),
    (r'^categoria/editar/(?P<category_id>\d+)/$', 'mitsuisushibar.categories.views.edit'),
    (r'^categoria/salvar/$', 'mitsuisushibar.categories.views.create'),
    (r'^categoria/atualizar/(?P<category_id>\d+)/$', 'mitsuisushibar.categories.views.update'),
    (r'^categoria/deletar/(?P<category_id>\d+)/$', 'mitsuisushibar.categories.views.delete'),

    (r'^unidades_de_medidas/$', 'mitsuisushibar.measures.views.index'),
    
    (r'^produtos/$', 'mitsuisushibar.products.views.index'),
    (r'^produto/novo/$', 'mitsuisushibar.products.views.new'),
    (r'^produto/editar/(?P<product_id>\d+)/$', 'mitsuisushibar.products.views.edit'),
    (r'^produto/salvar/$', 'mitsuisushibar.products.views.create'),
    (r'^produto/atualizar/(?P<product_id>\d+)/$', 'mitsuisushibar.products.views.update'),
    (r'^produto/deletar/(?P<product_id>\d+)/$', 'mitsuisushibar.products.views.delete'),
    
    (r'^produto/(?P<product_id>\d+)/item/salvar/$', 'mitsuisushibar.products.views.salvar_item'),
    (r'^produto/(?P<product_id>\d+)/item/deletar/(?P<item_id>\d+)/$', 'mitsuisushibar.products.views.delete_item'),
    
    (r'^usuarios/$', 'mitsuisushibar.users.views.index'),
    (r'^usuario/novo/$', 'mitsuisushibar.users.views.new'),
    (r'^usuario/editar/(?P<user_id>\d+)/$', 'mitsuisushibar.users.views.edit'),
    (r'^usuario/salvar/$', 'mitsuisushibar.users.views.create'),
    (r'^usuario/atualizar/(?P<user_id>\d+)/$', 'mitsuisushibar.users.views.update'),
    (r'^usuario/deletar/(?P<user_id>\d+)/$', 'mitsuisushibar.users.views.delete'),    
    
)
