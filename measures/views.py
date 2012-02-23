from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


from models import Measure

#path /unidades_de_medidas/
@login_required
def index(request):
    measures = Measure.objects.all().order_by('unit')
    return render_to_response('measures.html', locals(),
                              context_instance=RequestContext(request))
