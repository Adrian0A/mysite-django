from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpRequest as request

""" def myview(request) :
    

    resp.set_cookie('dj4e_cookie', '480ef4ce', max_age=1000)
    numVis = request.session.get('numVis', 0) +1
    request.session['numVis'] = numVis
    if numVis > 4 :
        del(request.session['numVis'])

    return HttpResponse('view count='+str(numVis)) """


def myview(request) :
    
    resp = request
    numVis = resp.session.get('numVis', 0) +1
    resp.session['numVis'] = numVis
    if numVis > 4 :
        del(resp.session['numVis'])

    resposta  = render(resp,'hello/main.html',{'numVis': numVis,} )
    resposta.set_cookie('dj4e_cookie', '480ef4ce', max_age=1000)

    return resposta