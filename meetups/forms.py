from django import forms
from django.db.models import fields
from .models import Participant

# model form
# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model=Participant
#         fields=['email']

# form object
class RegistrationForm(forms.Form):
    email=forms.EmailField(label='your email')