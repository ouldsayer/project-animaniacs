from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mitsuisushibar.views.home', name='home'),
    # url(r'^mitsuisushibar/', include('mitsuisushibar.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    (r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    
    #(r'^login/(?P<username>)/(?P<username>)/$', 'mitsuisushibar.categories.views.delete')
    (r'^itens/$', 'mitsuisushibar.items.views.index'),
    (r'^$', 'mitsuisushibar.views.login'),
    (r'^categorias/$', 'mitsuisushibar.categories.views.index'),
    (r'^categoria/editar/(?P<category_id>\d+)/$', 'mitsuisushibar.categories.views.edit'),
    (r'^categoria/salvar/(?P<category_id>\d+)/$', 'mitsuisushibar.categories.views.save'),
    (r'^categoria/deletar/(?P<category_id>\d+)/$', 'mitsuisushibar.categories.views.delete'),
    
    (r'^item/editar/(?P<item_id>\d+)/$', 'mitsuisushibar.items.views.edit'),
    (r'^item/salvar/(?P<item_id>\d+)/$', 'mitsuisushibar.items.views.save'),
    (r'^item/deletar/(?P<item_id>\d+)/$', 'mitsuisushibar.items.views.delete'),
    
    (r'^medidas/$', 'mitsuisushibar.measures.views.index'),
    
    (r'^usuarios/$', 'mitsuisushibar.users.views.index'),

    
)
