from django.shortcuts import render
from django.utils import timezone
from django.db.models import Q

from .models import SystemMessage, EventMessage, Game

def landing(request):
    context = { 'request': request }
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

    return render( request, 'frontpage.html', context )

def homepage(request):
    context = { 'request': request }

    return render( request, 'homepage.html', context )
