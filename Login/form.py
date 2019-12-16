
from django import forms
from Login.models import login

class LoginForm(forms.ModelForm):

	class Meta:
		model=login
		fields="__all__"
