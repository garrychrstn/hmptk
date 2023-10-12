from django import forms
from dal import autocomplete
from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

class MessageInput(forms.Form):
    msg = forms.CharField(
        max_length = 400,
        label = 'hey',
        label_suffix= '',
        widget=forms.TextInput(attrs={
            'placeholder' : 'Masukan pesanmu disini'
        })
    )

class addEvent(forms.Form):
    line_option = [
        ('Online', 'Online'),
        ('Offline', 'Offline'),
        ('Hybrid', 'Hybrid')
    ]
    cat = forms.CharField(
        required=True,
        max_length=20,
        label='Category'
    )
    title = forms.CharField(
        max_length=60,
        label='Title',
        required=True
    )
    date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'})
    )
    desc = forms.CharField(
        max_length=60,
        label='Description',
        required='True'
    )
    line = forms.ChoiceField(
        required=True, 
        widget=forms.Select,
        choices=line_option,
        label='Online/Offline'
    )
    img = forms.CharField(
        required=True,
        label='Image Link',
        max_length=40
    )
    link = forms.CharField(
        required=True,
        label='Registration Link',
        max_length=50
    )