from django import forms
from contact_us.models import ContactForm
from django.forms import widgets

class contact_form(forms.ModelForm):
	class Meta:
		model = ContactForm
		fields = "__all__"


