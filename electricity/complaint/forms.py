from django import forms
from .models import Complaint
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    class Meta:
      model = User
      fields = ('username', 'password1', 'password2')
      





class UpdatecomplaintInfoForm(forms.ModelForm):
    CHOICE_STATUS = (
        (None, '-- Provide complaint\'s status -- '),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    )
    status = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select'}), choices=CHOICE_STATUS,)

    class Meta:
            model = Complaint
            fields = '__all__'


class EditForm(forms.ModelForm):
    CHOICE_STATUS = (
        (None, '-- Provide complaint\'s status -- '),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    )
    status = forms.ChoiceField(widget=forms.Select(attrs={'type': 'select'}), choices=CHOICE_STATUS,)

    class Meta:
            model = Complaint
            fields = '__all__'

