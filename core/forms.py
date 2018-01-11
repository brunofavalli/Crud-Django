#-*- encoding: utf-8 -*-
from django import forms
from core.models import Crud
from models import Crud



class FormCrud(forms.ModelForm):
	class Meta:
		model = Crud
		fields = '__all__'
