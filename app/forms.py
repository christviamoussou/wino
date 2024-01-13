from django import forms
from django.contrib.auth.forms import AuthenticationForm

class EmailAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(label="Email", required=True)

    class Meta:
        fields = ['email', 'password']
