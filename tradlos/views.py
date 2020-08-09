from django.shortcuts import render

def landing(request):
    context = { 'request': request }
    return render( request, 'frontpage.html', context )
