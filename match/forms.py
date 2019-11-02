from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Propose

class ProposeForm(forms.ModelForm):

    class Meta:
        model = Propose
        fields = ['message',]