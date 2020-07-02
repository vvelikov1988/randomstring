from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def rword(request):
    if 'count' not in request.session:
        request.session['count']= 0
    request.session['rstring'] = get_random_string(length=14)
    request.session['count'] += 1
    return render(request, 'randomword.html')

def reset(request):
    request.session.flush()
    return redirect('/random_word')




