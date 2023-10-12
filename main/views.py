from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from datetime import date, timezone, datetime
from django.db.models import Prefetch
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import *
from .models import *

def index(response):
    event = Event.objects.all()
    if response.method == 'POST':
        msgform = MessageInput(response.POST)

        if msgform.is_valid():
            msg = msgform.cleaned_data['msg']
        
            m = Message(msg=msg)
            m.save()

            msgform = MessageInput()
    else:
        msgform = MessageInput()
    context = {
        'msgform' : msgform,
        'event' : event
    }
    return render(response, 'index.html', context)

def db (response):
    if response.method == 'POST':
        eventF = addEvent(response.POST)
        if eventF.is_valid():
            img=eventF.cleaned_data['img']
            cat=eventF.cleaned_data['cat']
            line=eventF.cleaned_data['line']
            title=eventF.cleaned_data['title']
            date=eventF.cleaned_data['date']
            link=eventF.cleaned_data['link']
            desc=eventF.cleaned_data['desc']

            e = Event(img=img, cat=cat, line=line, title=title, date=date, link=link, desc=desc)
            e.save()
            
            eventF = addEvent()
    else:
        eventF = addEvent()
        
    context = {
        'eventF' : eventF
    }

    return render(response, 'db.html', context)