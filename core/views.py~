#-*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from models import Crud
from forms import FormCrud


# Create your views here.

# Página inicial
def lista(request):
	lista_itens = Crud.objects.all()
	return render_to_response("lista.html",{"lista_itens":lista_itens})

# Método POST para inclusão de dados
def adiciona(request):
	if request.method == 'POST':
		form = FormCrud(request.POST, request.FILES)
		if form.is_valid():
			dados = form.cleaned_data
			item = Crud(nome = dados['nome'],cpf = dados['cpf'],idade = dados['idade'],sexo = dados['sexo'],date = dados['date'])
			item.save()
			return render_to_response("salvo.html",{})
	else:
		form = FormCrud() 

	return render_to_response("adiciona.html",{'form':form},context_instance=RequestContext(request))
		
