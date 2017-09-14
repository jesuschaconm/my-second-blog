# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils import timezone
from .models import Persona
from .forms import PersonaForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def post_list(request):
    personas = Persona.objects.all()
    return render(request, 'personal/post_list.html', locals())
    
def post_agregar(request):
    if request.POST:
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PersonaForm()
    return render(request, 'personal/post_detail.html', locals())



def post_editar(request,pk):
    persona = Persona.objects.get(pk=pk)
    if request.POST:
        form = PersonaForm(request.POST,instance=persona)
        if form.is_valid():
            form.save()
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'personal/post_edit.html', locals())

def post_eliminar(request,pk):
    persona = Persona.objects.get(pk=pk)
    persona.delete()
    return HttpResponseRedirect(reverse('home'))


