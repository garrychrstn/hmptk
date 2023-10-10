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