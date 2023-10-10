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
    }
    return render(response, 'index.html', context)
