from ast import Mod
from cProfile import label
from dataclasses import fields
from pyexpat import model
from re import M
from tkinter import Widget
from xml.dom.minidom import Attr
from django import forms
from django.forms import ModelForm
from .models import  Profile




        

class myProfileForm(ModelForm):
    

    class Meta:
        model =Profile
        fields = '__all__'
        exclude = ['user']
        