from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError

from .models import UserDetails
from .widgets import PlaceholderInput, ShowHidePasswordWidget

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    def save(self):
        pass

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        error_messages = {
            'username': {
                'unqiue': _("Please enter another username. This one is already taken."),
            },
        }
        widgets = {
            "username": PlaceholderInput,           #forms.TextInput(attrs={'placeholder': 'Username'}),
            "password": ShowHidePasswordWidget      #forms.PasswordInput,
        }

    def save(self, commit=True, *args, **kwargs):
        m = super().save(commit=False)
        m.password = make_password(self.cleaned_data.get('password'))
        m.username = self.cleaned_data.get('username').lower()

        if commit:
            m.save()
        return m

class UserDetailsForm(forms.ModelForm):
    lastname = forms.CharField(required=False)
    class Meta:
        model = UserDetails
        fields = ['firstname', 'lastname', 'username', 'email', 'phone', 'zipcode', 'address']
        error_messages = {
            'zipcode': {
                'invaild_length':_("Wrong zipcode. Ite needs to be 4 characters long."),
            },
        }

    def clean(self):
        address = self.cleaned_data.get("address")
        zipcode = self.cleaned_data.get("zipcode")

        if address and zipcode:
            if zipcode > '1234':
                msg = "We do not deliver in the area."
                self.add_error('address', msg)
                self.add_error('zipcode', msg)
                raise ValidationError(("There's a problem with the address entered"),
                                        code='wrong address')