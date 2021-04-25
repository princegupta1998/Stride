from django import forms
from registration.models import players
from django.forms import widgets

class players_form(forms.ModelForm):
	class Meta:
		model = players
		fields = "__all__"
		

class playerssearchform(forms.ModelForm):
	class Meta:
		model = players
		fields = ['sports']