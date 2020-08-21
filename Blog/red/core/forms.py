from .models import Blog, Category
from django.forms import ModelForm, TextInput
from django import forms
class CategoryForm(ModelForm):
	class Meta:
		model = Category
		fields = ['category']
		widgets = {"category": TextInput( attrs={
						'class': 'form-control'

			}) 

		}


#class ContanctForm(forms.Form):
#	title = forms.CharField(max_length=100)
#	content = forms.CharField(max_length=255)
