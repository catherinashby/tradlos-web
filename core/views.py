import re

from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Q

from .models import User, SystemMessage, EventMessage, Game

def landing(request):
    context = { 'request': request }
    if request.user.is_authenticated:
        return redirect('homepage')

    template = 'frontpage.html'
    limit = timezone.now()

    query = Q(message_removed__isnull=True) | Q(message_removed__gte=limit)
    sysmsgs = SystemMessage.objects.filter(query)
    context['sysmsgs'] = sysmsgs

    query = Q(event_removed__isnull=True) | Q(event_removed__gte=limit)
    events  = EventMessage.objects.filter(query)
    context['events'] = events

    query = Q(game_removed__isnull=True) | Q(game_removed__gte=limit)
    gamelist = Game.objects.filter(query).filter(game_status='PB')
    context['gamelist'] = gamelist

    return render( request, template, context )

def entry_page(request):
    context = { 'request': request }
    template = 'registration/entryPage.html'

    if request.POST:
        btn = 'register' if 'sign_up' in request.POST else (
            'login' if 'sign_in' in request.POST else None )
        current_name = request.POST['user_name']
        context['current_name'] = '{}'.format(current_name)
        valid = ( ( re.fullmatch( r'[0-9A-Za-z@\.\+\-_]+', current_name ) )
            and ( len(current_name) >= 8 ) )
        if valid:
            found = ( User.objects.filter(username=current_name).count() > 0 )
            if found:
                if btn == 'login':
                    template = 'registration/loginPage.html'
                else:
                    context['error_message'] = "Name already in use"
            else:
                if btn == 'register':
                    template = 'registration/registerPage.html'
                else:
                    context['error_message'] = "Name not found"
        else:
            context['show_help'] = ""

    return render( request, template, context )

def homepage(request):
    context = { 'request': request }
    template = 'homepage.html'

    return render( request, template, context )
